# -*- coding: utf-8 -*-

from imio.urban.dataimport.mapper import Mapper
from imio.urban.dataimport.factory import BaseFactory

from Products.CMFPlone.utils import normalizeString

import re


# Factory
class ParcellingFactory(BaseFactory):
    def getCreationPlace(self, factory_args):
        return self.site.urban.parcellings

    def getPortalType(self, container, **kwargs):
        return 'ParcellingTerm'


class IdMapper(Mapper):
    def mapId(self, line):
        name = '%s' % self.getData('n° permis')
        contact_id = normalizeString(self.site.portal_urban.generateUniqueId(name))
        return contact_id

#
# PARCEL
#

#factory


class ParcelFactory(BaseFactory):
    def create(self, parcel_args, container=None, line=None):
        searchview = self.site.restrictedTraverse('searchparcels')
        # need to trick the search browser view about the args in its request
        for k, v in parcel_args.iteritems():
            searchview.context.REQUEST[k] = v
        # check if we can find a parcel in the db cadastre with these infos
        found = searchview.findParcel(**parcel_args)
        if not found:
            found = searchview.findParcel(browseoldparcels=True, **parcel_args)
        if len(found) == 1:
            parcel_args['divisionCode'] = parcel_args['division']
            parcel_args['division'] = parcel_args['division']
            parcel_args['isOfficialParcel'] = True
        else:
            self.logError(
                self,
                line,
                'Too much parcels found or not enough parcels found',
                {'args': parcel_args, 'search result': len(found)}
            )
            parcel_args['isOfficialParcel'] = False
        parcel_args['portal_type'] = 'PortionOut'
        parcel_args['id'] = ''.join(
            [
                parcel_args['division'],
                parcel_args['section'],
                parcel_args['radical'],
                parcel_args['bis'],
                parcel_args['exposant'],
                parcel_args['puissance']
            ]
        )
        return super(ParcelFactory, self).create(parcel_args, container=container, line=line)

# mappers


class ParcelRefMapper(Mapper):

    regex = '\s*(?P<radical>\d+)(?P<exposant>[A-Z])(?:/(?P<bis>\d))?(?P<puissance>\d+)?\s*'

    def map(self, line, **kwargs):

        self.line = line
        division = self.getData('Division')
        section = self.getData('section')
        reference_tails = self.getData('numéro cadastral')
        if not section or not division or not reference_tails:
            return []

        references = []
        for ref_tail in reference_tails.split('-'):

            match = re.search(self.regex, ref_tail)

            reference = {
                'division': division,
                'section':  section,
                'radical': match.group('radical'),
                'bis':  match.group('bis') or '',
                'exposant': match.group('exposant') or '',
                'puissance': match.group('puissance') or '',
            }
            references.append(reference)

        return references
