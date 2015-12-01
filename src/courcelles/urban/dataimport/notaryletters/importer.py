# -*- coding: utf-8 -*-

from zope.interface import implements

from courcelles.urban.dataimport.notaryletters import mapping
from courcelles.urban.dataimport.notaryletters import valuesmapping
from courcelles.urban.dataimport.interfaces import ILicencesImporter
from imio.urban.dataimport.access.importer import AccessDataImporter
from imio.urban.dataimport.mapping import ObjectsMapping
from imio.urban.dataimport.mapping import ValuesMapping


class NotarylettersImporter(AccessDataImporter):
    """ """

    implements(ILicencesImporter)

    def __init__(self, db_name='registre_data.mdb', table_name='fiche notaire', key_column='s_GUID', savepoint_length=0):
        super(NotarylettersImporter, self).__init__(db_name, table_name, key_column, savepoint_length)


class NotarylettersMapping(ObjectsMapping):
    """ """

    def getObjectsNesting(self):
        return mapping.OBJECTS_NESTING

    def getFieldsMapping(self):
        return mapping.FIELDS_MAPPINGS


class NotarylettersValuesMapping(ValuesMapping):
    """ """

    def getValueMapping(self, mapping_name):
        return valuesmapping.VALUES_MAPS.get(mapping_name)
