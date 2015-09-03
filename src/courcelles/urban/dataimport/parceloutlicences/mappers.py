# -*- coding: utf-8 -*-

from imio.urban.dataimport.access.mapper import AccessMapper as Mapper


class PortalTypeMapper(Mapper):
    def mapPortal_type(self, line):
        return 'ParcelOutLicence'


class ObservationsMapper(Mapper):
    def mapDescription(self, line):
        description = """<p>{car}</p><p>nombre de lots: {nbr_lots}</p>
<p>lot modif: {lot_modif}</p>\<p>{rem}</p>""".format(
            car=self.getData('caractéristiques'),
            nbr_lots=self.getData('nomb lot'),
            lot_modif=self.getData('lotmodif'),
            rem=self.getData('REMARQUES')
        )
        return description
