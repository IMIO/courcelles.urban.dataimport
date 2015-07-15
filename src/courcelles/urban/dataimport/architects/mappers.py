# -*- coding: utf-8 -*-

from imio.urban.dataimport.mapper import Mapper
from imio.urban.dataimport.factory import BaseFactory

from Products.CMFPlone.utils import normalizeString


# Factory
class ArchitectFactory(BaseFactory):
    def getCreationPlace(self, factory_args):
        return self.site.urban.architects

    def getPortalType(self, container, **kwargs):
        return 'Architect'


class IdMapper(Mapper):
    def mapId(self, line):
        name = '%s' % self.getData('nom')
        name = name.replace(' ', '').replace('-', '')
        contact_id = normalizeString(self.site.portal_urban.generateUniqueId(name))
        return contact_id


class PhoneMapper(Mapper):
    def mapPhone(self, line):
        phone = self.getData('téléphone')
        gsm = self.getData('gsm')

        if (phone and phone != '-') and (gsm and gsm != '-'):
            phones = '{phone}, {gsm}'.format(
                phone=phone,
                gsm=gsm,
            )
            return phones
        elif phone and phone != '-':
            return phone
        elif gsm and gsm != '-':
            return gsm

        return ''
