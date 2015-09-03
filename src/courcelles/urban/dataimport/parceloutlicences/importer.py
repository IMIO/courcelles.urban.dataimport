# -*- coding: utf-8 -*-

from courcelles.urban.dataimport.interfaces import ILicencesImporter
from courcelles.urban.dataimport.parceloutlicences import mapping
from courcelles.urban.dataimport.licences import valuesmapping

from imio.urban.dataimport.access.importer import AccessDataImporter
from imio.urban.dataimport.mapping import ObjectsMapping
from imio.urban.dataimport.mapping import ValuesMapping

from zope.interface import implements


class ParceloutLicencesImporter(AccessDataImporter):
    """ """

    implements(ILicencesImporter)

    def __init__(self, db_name='registre_data.mdb', table_name='registre permis lotir', key_column='s_GUID', savepoint_length=0):
        super(ParceloutLicencesImporter, self).__init__(db_name, table_name, key_column, savepoint_length)


class ParceloutLicencesMapping(ObjectsMapping):
    """ """

    def getObjectsNesting(self):
        return mapping.OBJECTS_NESTING

    def getFieldsMapping(self):
        return mapping.FIELDS_MAPPINGS


class ParceloutLicencesValuesMapping(ValuesMapping):
    """ """

    def getValueMapping(self, mapping_name):
        return valuesmapping.VALUES_MAPS.get(mapping_name)
