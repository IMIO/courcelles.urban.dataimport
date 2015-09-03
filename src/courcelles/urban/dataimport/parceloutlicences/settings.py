# -*- coding: utf-8 -*-

from courcelles.urban.dataimport.parceloutlicences.importer import ParceloutLicencesImporter
from imio.urban.dataimport.browser.adapter import ImporterFromSettingsForm


class ParceloutLicencesImporterFromImportSettings(ImporterFromSettingsForm):
    """ """

    def __init__(self, settings_form, importer_class=ParceloutLicencesImporter):
        """
        """
        super(ParceloutLicencesImporterFromImportSettings, self).__init__(settings_form, importer_class)
