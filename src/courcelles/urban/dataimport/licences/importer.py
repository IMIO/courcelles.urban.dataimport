# -*- coding: utf-8 -*-

from zope.interface import implements

# from courcelles.urban.dataimport.licences import mapping
from courcelles.urban.dataimport.interfaces import ILicencesImporter
from imio.urban.dataimport.access.importer import AccessDataImporter
from imio.urban.dataimport.mapping import ObjectsMapping
from imio.urban.dataimport.mapping import ValuesMapping


class LicencesImporter(AccessDataImporter):
    """ """

    implements(ILicencesImporter)


class LicencesMapping(ObjectsMapping):
    """ """

    def getObjectsNesting(self):
        return  # mapping.OBJECTS_NESTING

    def getFieldsMapping(self):
        return  # mapping.FIELDS_MAPPINGS


class LicencesValuesMapping(ValuesMapping):
    """ """

    def getValueMapping(self, mapping_name):
        return
