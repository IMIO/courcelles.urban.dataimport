# -*- coding: utf-8 -*-

from imio.urban.dataimport.access.mapper import AccessMapper as Mapper
from imio.urban.dataimport.access.mapper import AccessPostCreationMapper as PostCreationMapper
from imio.urban.dataimport.access.mapper import AccessFinalMapper as FinalMapper
from imio.urban.dataimport.exceptions import NoObjectToCreateException

from imio.urban.dataimport.factory import BaseFactory
from imio.urban.dataimport.utils import cleanAndSplitWord

from DateTime import DateTime

from Products.CMFPlone.utils import normalizeString

from plone import api

import re

#
# LICENCE
#

# factory


class NotaryletterFactory(BaseFactory):
    def getCreationPlace(self, factory_args):
        path = '%s/urban/notaryletters' % self.site.absolute_url_path()
        return self.site.restrictedTraverse(path)

# mappers


class WorklocationMapper(Mapper):
    def mapWorklocations(self, line):
        locality = self.getData('localitebien')
        raw_street = self.getData('ruebien') or u''
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


class ObservationsMapper(Mapper):
    def mapDescription(self, line):
        description = '<p>{rem}</p>'.format(
            rem=self.getData('remarqueurbanisme')
        )
        return description


class CompletionStateMapper(PostCreationMapper):
    def map(self, line, plone_object):
        self.line = line
        if self.getData('dateenvoi'):
            api.content.transition(obj=plone_object, to_state='accepted')


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
                    error_trace.append('<p>lotissement : %s autorisé le %s (%s lots)</p>' % (data['reference'], data['auth_date'], data['lot']))
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
        name = self.getData('nompro')
        if not name:
            raise NoObjectToCreateException
        return normalizeString(self.site.portal_urban.generateUniqueId(name))


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
        raw_references = self.getData('cadastre').upper()

        reference_groups = self.splitReferenceGroups(raw_references)
        tokenized_references = [self.tokenizeReference(ref) for ref in reference_groups]

        base_ref = tokenized_references[0]
        base_ref.reverse()

        division = self.getDivision()
        section = self.getData('section').strip()
        if not section or not division:
            return []
        self.division_name = self.getData('localitebien')

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
                    'division': self.getData('localitebien'),
                    'section': self.getData('section'),
                    'ref': self.getData('cadastre')
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
                        'division': self.getData('localitebien'),
                        'section': self.getData('section'),
                        'ref': self.getData('cadastre')
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
        raw_division = self.getData('localitebien').lower().split(' ')[0].replace('_', '-')
        try:
            raw_division = raw_division.split(' ')[0]
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
        eventtype_id = 'depot-de-la-demande'
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
