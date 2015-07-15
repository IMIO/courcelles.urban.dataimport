# -*- coding: utf-8 -*-

from zope.interface import implements

from courcelles.urban.dataimport.architects import mapping
from courcelles.urban.dataimport.interfaces import ICourcellesDataImporter
from imio.urban.dataimport.csv.importer import CSVDataImporter
from imio.urban.dataimport.mapping import ObjectsMapping
from imio.urban.dataimport.mapping import ValuesMapping


class ArchitectsImporter(CSVDataImporter):
    """ """

    implements(ICourcellesDataImporter)


class ArchitectsMapping(ObjectsMapping):
    """ """

    def getObjectsNesting(self):
        return mapping.OBJECTS_NESTING

    def getFieldsMapping(self):
        return mapping.FIELDS_MAPPINGS


class ArchitectsValuesMapping(ValuesMapping):
    """ """

    def getValueMapping(self, mapping_name):
        return
