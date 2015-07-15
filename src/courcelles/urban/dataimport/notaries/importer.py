# -*- coding: utf-8 -*-

from courcelles.urban.dataimport.notaries import mapping
from imio.urban.dataimport.access.importer import AccessDataImporter
from imio.urban.dataimport.mapping import ObjectsMapping
from imio.urban.dataimport.mapping import ValuesMapping


class NotariesImporter(AccessDataImporter):
    """ """


class NotariesMapping(ObjectsMapping):
    """ """

    def getObjectsNesting(self):
        return mapping.OBJECTS_NESTING

    def getFieldsMapping(self):
        return mapping.FIELDS_MAPPINGS


class NotariesValuesMapping(ValuesMapping):
    """ """

    def getValueMapping(self, mapping_name):
        return
