# -*- coding: utf-8 -*-

from imio.urban.dataimport.access.mapper import AccessMapper as Mapper
from imio.urban.dataimport.access.mapper import AccessPostCreationMapper as PostCreationMapper
from imio.urban.dataimport.access.mapper import AccessFinalMapper as FinalMapper
from imio.urban.dataimport.exceptions import NoObjectToCreateException

from imio.urban.dataimport.factory import BaseFactory
from imio.urban.dataimport.utils import cleanAndSplitWord
from imio.urban.dataimport.utils import normalizeDate

from DateTime import DateTime

from Products.CMFPlone.utils import normalizeString

from plone import api

import re

#
# LICENCE
#

# factory


class LicenceFactory(BaseFactory):
    def getCreationPlace(self, factory_args):
        portal_type = factory_args.get('portal_type')
        path = '%s/urban/%ss' % (self.site.absolute_url_path(), portal_type.lower())
        return self.site.restrictedTraverse(path)

# mappers


class PortalTypeMapper(Mapper):
    def mapPortal_type(self, line):
        type_value = self.getData('type')
        portal_type = self.getValueMapping('type_map')[type_value]['portal_type']
        if not portal_type:
            raise NoObjectToCreateException
        return portal_type

    def mapFoldercategory(self, line):
        type_value = self.getData('type')
        foldercategory = self.getValueMapping('type_map')[type_value]['foldercategory']
        if not foldercategory:
            raise NoObjectToCreateException
        return foldercategory


class WorklocationMapper(Mapper):
    def mapWorklocations(self, line):
        locality = self.getData('lieu')
        raw_street = self.getData('ruelieu') or u''
        regex = '([^\d,]+\s*)+,?\s*(.*)'
        parsed_street = re.search(regex, raw_street)
        if parsed_street:
            street, num = parsed_street.groups()
            street_keywords = cleanAndSplitWord(street + ' ' + locality)
            street_keywords = [word for word in street_keywords if len(word) > 1]
            brains = self.catalog(portal_type='Street', Title=street_keywords, review_state='enabled')
            if len(brains) == 1:
                return ({'street': brains[0].UID, 'number': num or ''},)
            if street:
                self.logError(self, line, 'Couldnt find street or found too much streets', {
                    'address': '%s' % raw_street,
                    'street': street_keywords,
                    'search result': len(brains)
                })
        else:
            self.logError(self, line, 'Couldnt parse street and number', {
                'address': '%s' % raw_street,
            })
        return ({},)


class DelayMapper(Mapper):
    def mapAnnonceddelay(self, line):
        delay = self.getData('délai')
        if delay in ['30', '70', '75', '90', '115', '230']:
            return delay + 'j'
        return []


class PcaMapper(Mapper):
    def mapIsinpca(self, line):
        return bool(self.getData('DatePPA'))

    def mapPca(self, line):
        if not self.mapIsinpca(line):
            return []
        pca_date = normalizeDate(self.getData('DatePPA'))
        pcas = self.catalog(Title=pca_date)
        if len(pcas) != 1:
            self.logError(self, line, 'Couldnt find pca or found too much pca', {'date': pca_date})
            return []
        return pcas[0].id


class ParcellingsMapper(Mapper):
    def mapIsinsubdivision(self, line):
        return any([self.getData('NumLot'), self.getData('DateLot'), self.getData('DateLotUrbanisme')])

    def mapParcellings(self, line):
        if not self.mapIsinsubdivision(line):
            return []
        auth_date = normalizeDate(self.getData('DateLot'))
        approval_date = normalizeDate(self.getData('DateLotUrbanisme'))
        raw_city = self.getData('AncCommune')
        city = raw_city.split('-')
        keywords = [approval_date] + city
        if raw_city or approval_date:
            parcellings = self.catalog(Title=keywords)
            if len(parcellings) == 1:
                return parcellings[0].getObject().UID()
            keywords = [auth_date] + city
            parcellings = self.catalog(Title=keywords)
            if len(parcellings) == 1:
                return parcellings[0].getObject().UID()
            self.logError(self, line, 'Couldnt find parcelling or found too much parcelling', {'approval date': approval_date, 'auth_date': auth_date, 'city': raw_city})
        return []


class ParcellingRemarksMapper(Mapper):
    def mapLocationtechnicalremarks(self, line):
        return '<p>%s</p>' % self.getData('PPAObservations')


class ObservationsMapper(Mapper):
    def mapDescription(self, line):
        description = '<p>{car}</p><p>{rem}</p>'.format(
            car=self.getData('caractéristiques'),
            rem=self.getData('REMARQUES')
        )
        return description


class ArchitectMapper(PostCreationMapper):
    def mapArchitects(self, line, plone_object):
        archi_name = self.getData('architecte')
        fullname = cleanAndSplitWord(archi_name)
        if not fullname:
            return []
        noisy_words = ['monsieur', 'madame', 'architecte', '&', ',', '.', 'or', 'mr', 'mme', '/']
        name_keywords = [word.lower() for word in fullname if word.lower() not in noisy_words and len(word) > 2]
        architects = self.catalog(portal_type='Architect', Title=name_keywords)
        if len(architects) == 1:
            return architects[0].getObject()
        self.logError(self, line, 'No architects found or too much architects found',
                      {
                          'raw_name': archi_name,
                          'name': name_keywords,
                          'search_result': len(architects)
                      })
        return []


class InquiryStartMapper(PostCreationMapper):
    def mapInvestigationstart(self, line, plone_object):
        date = self.getData('débutenquete')
        date = date and DateTime(date) or None
        return date


class InquiryEndMapper(PostCreationMapper):
    def mapInvestigationend(self, line, plone_object):
        date = self.getData('finenquete')
        date = date and DateTime(date) or None
        return date


class CompletionStateMapper(PostCreationMapper):
    def map(self, line, plone_object):
        self.line = line
        state = ''
        if self.getData('datepermis'):
            state = 'accepted'
        elif self.getData('daterefus'):
            state = 'refused'
        else:
            return
        workflow_tool = api.portal.get_tool('portal_workflow')
        workflow_def = workflow_tool.getWorkflowsFor(plone_object)[0]
        workflow_id = workflow_def.getId()
        workflow_state = workflow_tool.getStatusOf(workflow_id, plone_object)
        workflow_state['review_state'] = state
        workflow_tool.setStatusOf(workflow_id, plone_object, workflow_state.copy())


class ErrorsMapper(FinalMapper):
    def mapDescription(self, line, plone_object):

        line_number = self.importer.current_line
        errors = self.importer.errors.get(line_number, None)
        description = plone_object.Description()

        error_trace = []

        if errors:
            for error in errors:
                data = error.data
                if 'street' in error.message:
                    error_trace.append('<p>adresse : %s</p>' % data['address'])
                elif 'architects' in error.message:
                    error_trace.append('<p>architecte : %s</p>' % data['raw_name'])
                elif 'parse cadastral' in error.message:
                    error_trace.append('<p>ref cadastrale : %s %s %s</p>' % (data['division'], data['section'], data['ref']))
                elif 'parcelling' in error.message:
                    error_trace.append('<p>lotissement : %s %s, autorisé le %s</p>' % (data['approval date'], data['city'], data['auth_date']))
        error_trace = ''.join(error_trace)
        if type(error_trace) == type(u''):
            error_trace = error_trace.encode('utf-8')
        if type(description) == type(u''):
            description = description.encode('utf-8')
	
        return '%s%s' % (error_trace, description)

#
# CONTACT
#

# factory


class ContactFactory(BaseFactory):

    def getPortalType(self, place, **kwargs):
        if place.portal_type in ['UrbanCertificateOne', 'UrbanCertificateTwo', 'NotaryLetter']:
            return 'Proprietary'
        return 'Applicant'

# mappers


class ContactIdMapper(Mapper):
    def mapId(self, line):
        name = self.getData('Nom')
        if not name:
            raise NoObjectToCreateException
        return normalizeString(self.site.portal_urban.generateUniqueId(name))


class ContactTitleMapper(Mapper):
    def mapPersontitle(self, line):
        titre = self.getData('Titre') or ''
        titre_mapping = self.getValueMapping('titre_map')
        if titre in titre_mapping.keys():
            return titre_mapping[titre]
        return 'notitle'


class ContactNameMapper(Mapper):
    def mapName1(self, line):
        raw_name = self.getData('Nom')
        names = raw_name.split(' ')
        if len(names) == 2:
            return names[0]
        return raw_name

    def mapName2(self, line):
        raw_name = self.getData('Nom')
        names = raw_name.split(' ')
        if len(names) == 2:
            return names[1]
        return ''


class ContactSreetMapper(Mapper):
    def mapStreet(self, line):
        regex = '((?:[^\d,]+\s*)+),?'
        raw_street = self.getData('ruedomicile') or ''
        match = re.match(regex, raw_street)
        if match:
            street = match.group(1)
        else:
            street = raw_street
        return street

    def mapNumber(self, line):
        regex = '(?:[^\d,]+\s*)+,?\s*(.*)'
        raw_street = self.getData('ruedomicile') or ''
        number = ''

        match = re.match(regex, raw_street)
        if match:
            number = match.group(1)
        return number


#
# PARCEL
#

#factory


class ParcelFactory(BaseFactory):
    def create(self, factory_args, container=None, line=None):
        searchview = self.site.restrictedTraverse('searchparcels')
        argnames = ['division', 'section', 'radical', 'puissance', 'exposant']
        args = {}

        for name in argnames:
            args[name] = factory_args.get(name, '')
        #need to trick the search browser view about the args in its request
        for k, v in args.iteritems():
            searchview.context.REQUEST[k] = v
        #check if we can find a parcel in the db cadastre with these infos
        found = searchview.findParcel(**args)
        if not found:
            found = searchview.findParcel(browseoldparcels=True, **args)
        if not found:
            if args['division'] == '52015':
                args['division'] = '52322'
                searchview.context.REQUEST['division'] = '52322'
                found = searchview.findParcel(**args)
            if not found:
                found = searchview.findParcel(browseoldparcels=True, **args)
        if len(found) == 1:
            args['divisionCode'] = args['division']
        else:
            self.logError(self, 'Too much parcels found or not enough parcels found', {'args': args, 'search result': len(found)})
        parcel_id = ''.join([args[name] for name in argnames]).replace('/', '')
        args['id'] = self.site.portal_urban.generateUniqueId(parcel_id)
        return super(ParcelFactory, self).create(args, container=container)


# mappers


class ParcelReferencesMapper(Mapper):
    def map(self, line, **kwargs):

        self.line = line
        raw_references = self.getData('numérocadastral').upper()

        reference_groups = self.splitReferenceGroups(raw_references)
        tokenized_references = [self.tokenizeReference(ref) for ref in reference_groups]

        base_ref = tokenized_references[0]
        base_ref.reverse()

        division = self.getDivision()
        section = self.getData('section').strip()
        if not section or not division:
            return []
        self.division_name = self.getData('lieu')

        bis = self.getBis(base_ref)
        if len(base_ref) > 3:
            self.logError(
                self,
                line,
                'Cannot parse cadastral reference',
                {
                    'division': self.getData('lieu'),
                    'section': self.getData('section'),
                    'ref': self.getData('numérocadastral')
                }
            )
            return []

        reference = {
            'bis': bis,
            'section': section,
            'radical': self.getRadical(base_ref),
            'exposant': self.getExposant(base_ref),
            'puissance': self.getPuissance(base_ref),
        }
        reference.update(division)

        references = [reference]

        for tokenized_ref in tokenized_references[1:]:
            ref = self.getSecondaryReference(tokenized_ref, reference)
            if ref:
                references.append(ref)

        return references

    def getSecondaryReference(self, secondary_ref, base_ref):
        bis = self.getBis(secondary_ref)

        ref_parts = ['radical', 'exposant', 'puissance']

        to_fill = []
        for part in ref_parts:
            if base_ref[part]:
                to_fill.append(part)
            else:
                break

        if len(secondary_ref) > 3 or len(secondary_ref) > len(to_fill):
            self.logError(
                self,
                self.line,
                'Cannot parse cadastral secondary reference',
                {
                    'division': self.getData('lieu'),
                    'section': self.getData('section'),
                    'ref': self.getData('numérocadastral')
                }
            )
            return

        reference = base_ref.copy()
        reference['bis'] = bis

        secondary_ref.reverse()
        for part in secondary_ref:
            part_name = to_fill.pop()
            old_part = reference[part_name]
            if self.isSameType(old_part, part):
                reference[part_name] = part
            else:
                self.logError(
                    self,
                    self.line,
                    'Cannot parse cadastral secondary reference',
                    {
                        'division': self.getData('lieu'),
                        'section': self.getData('section'),
                        'ref': self.getData('numérocadastral')
                    }
                )
                return

        return reference

    def isSameType(self, str1, str2):
        return (str1.isdigit() and str2.isdigit()) or (str1.isalpha() and str2.isalpha())

    def getPuissance(self, reference):
        if reference:
            return reference.pop()
        return ''

    def getExposant(self, reference):
        if reference:
            return reference.pop()
        return ''

    def getRadical(self, reference):
        if reference:
            return reference.pop()
        return ''

    def getBis(self, reference):
        if '/' in reference:
            bis_index = reference.index('/')
            bis = reference[bis_index - 1]
            del reference[bis_index - 1:bis_index + 1]
            return bis
        return ''

    def getDivision(self):
        raw_division = self.getData('lieu').lower()
        try:
            division = self.getValueMapping('division_map')[raw_division]
        except:
            self.logError(self, self.line, 'No division found')
            return
        result = {'division': division, 'divisioncode': division}
        return result

    def tokenizeReference(self, reference):
        reference = ''.join(cleanAndSplitWord(reference)).upper()
        # we do not use 'partie' in parcel search
        regex = '\W*(?P<radical>\d+)?\s*(?P<bis>/\s*\d+)?\W*(?P<exposant>[a-zA-Z](?![a-zA-Z]))?\W*(?P<puissance>\d+)?\W*(?P<partie>pie)?\W*'
        parsed_abbr = re.match(regex, reference).groups()
        reference = [part for part in parsed_abbr if part]
        return reference

    def splitReferenceGroups(self, raw_references):
        if '-' in raw_references:
            return raw_references.split('-')
        elif ',' in raw_references:
            return raw_references.split(',')
        elif '+' in raw_references:
            return raw_references.split(',')
        elif 'et' in raw_references:
            return raw_references.split('et')
        else:
            return [raw_references]

#
# UrbanEvent deposit
#


# factory
class UrbanEventFactory(BaseFactory):
    def getPortalType(self, **kwargs):
        return 'UrbanEvent'

    def create(self, factory_args, container, line):
        eventtype = factory_args.pop('eventtype')
        if not eventtype:
            return
        event = container.createUrbanEvent(eventtype, **factory_args)
        return event

#mappers


class DepositEventTypeMapper(Mapper):
    def mapEventtype(self, line):
        licence = self.importer.current_containers_stack[-1]
        urban_tool = api.portal.get_tool('portal_urban')
        eventtype_id = self.getValueMapping('eventtype_id_map')[licence.portal_type]['deposit_event']
        config = urban_tool.getUrbanConfig(licence)
        return getattr(config.urbaneventtypes, eventtype_id).UID()


class DepositDateMapper(Mapper):
    def mapEventdate(self, line):
        date = self.getData('daterecepisse')
        date = date and DateTime(date) or None
        if not date:
            raise NoObjectToCreateException
        return date

#
# UrbanEvent incomplete folder
#

#mappers


class IncompleteFolderEventTypeMapper(Mapper):
    def mapEventtype(self, line):
        licence = self.importer.current_containers_stack[-1]
        urban_tool = api.portal.get_tool('portal_urban')
        eventtype_id = self.getValueMapping('eventtype_id_map')[licence.portal_type]['folder_incomplete']
        config = urban_tool.getUrbanConfig(licence)
        return getattr(config.urbaneventtypes, eventtype_id).UID()


class IncompleteFolderDateMapper(Mapper):
    def mapEventdate(self, line):
        date = self.getData('datedossierincom')
        date = date and DateTime(date) or None
        if not date:
            raise NoObjectToCreateException
        return date

#
# UrbanEvent complete folder
#

#mappers


class CompleteFolderEventTypeMapper(Mapper):
    def mapEventtype(self, line):
        licence = self.importer.current_containers_stack[-1]
        urban_tool = api.portal.get_tool('portal_urban')
        eventtype_id = self.getValueMapping('eventtype_id_map')[licence.portal_type]['folder_complete']
        config = urban_tool.getUrbanConfig(licence)
        return getattr(config.urbaneventtypes, eventtype_id).UID()


class CompleteFolderDateMapper(Mapper):
    def mapEventdate(self, line):
        date = self.getData('dateaccuseréception')
        date = date and DateTime(date) or None
        if not date:
            raise NoObjectToCreateException
        return date

#
# UrbanEvent primo RW
#

#mappers


class PrimoEventTypeMapper(Mapper):
    def mapEventtype(self, line):
        licence = self.importer.current_containers_stack[-1]
        urban_tool = api.portal.get_tool('portal_urban')
        eventtype_id = 'transmis-1er-dossier-rw'
        config = urban_tool.getUrbanConfig(licence)
        return getattr(config.urbaneventtypes, eventtype_id).UID()


class PrimoDateMapper(Mapper):
    def mapEventdate(self, line):
        date = self.getData('dateenvoiprédossier')
        date = date and DateTime(date) or None
        if not date:
            raise NoObjectToCreateException
        return date

#
# UrbanEvent second RW
#

#mappers


class SecondRWEventTypeMapper(Mapper):
    def mapEventtype(self, line):
        licence = self.importer.current_containers_stack[-1]
        urban_tool = api.portal.get_tool('portal_urban')
        eventtype_id = 'transmis-2eme-dossier-rw'
        config = urban_tool.getUrbanConfig(licence)
        return getattr(config.urbaneventtypes, eventtype_id).UID()


class SecondRWEventDateMapper(Mapper):
    def mapEventdate(self, line):
        date = self.getData('dateavisfoncdelegue')
        date = date and DateTime(date) or None
        return date


class SecondRWDecisionMapper(Mapper):
    def mapExternaldecision(self, line):
        raw_decision = self.getData('typeavis')
        decision = self.getValueMapping('externaldecisions_map').get(raw_decision, [])
        return decision


class SecondRWDecisionDateMapper(Mapper):
    def mapDecisiondate(self, line):
        date = self.getData('dateavisfoncdelegue')
        date = date and DateTime(date) or None
        return date

#
# UrbanEvent decision
#

#mappers


class DecisionEventTypeMapper(Mapper):
    def mapEventtype(self, line):
        licence = self.importer.current_containers_stack[-1]
        urban_tool = api.portal.get_tool('portal_urban')
        eventtype_id = self.getValueMapping('eventtype_id_map')[licence.portal_type]['decision_event']
        config = urban_tool.getUrbanConfig(licence)
        return getattr(config.urbaneventtypes, eventtype_id).UID()


class DecisionDateMapper(Mapper):
    def mapDecisiondate(self, line):
        date = self.getData('datepermis') or self.getData('daterefus')
        date = date and DateTime(date) or None
        if not date:
            raise NoObjectToCreateException
        return date


class NotificationDateMapper(Mapper):
    def mapEventdate(self, line):
        date = self.getData('dateenvoipermis')
        date = date and DateTime(date) or None
        if not date:
            self.logError(self, line, 'No notification date found')
        return date


class DecisionMapper(Mapper):
    def mapDecision(self, line):
        if self.getData('datepermis'):
            return 'favorable'
        elif self.getData('daterefus'):
            return 'defavorable'
        raise NoObjectToCreateException

#
# UrbanEvent works start
#

#mappers


class WorksStartEventTypeMapper(Mapper):
    def mapEventtype(self, line):
        licence = self.importer.current_containers_stack[-1]
        urban_tool = api.portal.get_tool('portal_urban')
        eventtype_id = 'debut-des-travaux'
        config = urban_tool.getUrbanConfig(licence)
        return getattr(config.urbaneventtypes, eventtype_id).UID()


class WorksStartEventDateMapper(Mapper):
    def mapEventdate(self, line):
        date = self.getData('débuttravaux')
        date = date and DateTime(date) or None
        if not date:
            raise NoObjectToCreateException
        return date

#
# UrbanEvent works end
#

#mappers


class WorksEndEventTypeMapper(Mapper):
    def mapEventtype(self, line):
        licence = self.importer.current_containers_stack[-1]
        urban_tool = api.portal.get_tool('portal_urban')
        eventtype_id = 'fin-des-travaux'
        config = urban_tool.getUrbanConfig(licence)
        return getattr(config.urbaneventtypes, eventtype_id).UID()


class WorksEndEventDateMapper(Mapper):
    def mapEventdate(self, line):
        date = self.getData('fintravaux')
        date = date and DateTime(date) or None
        if not date:
            raise NoObjectToCreateException
        return date
