# -*- coding: utf-8 -*-

from courcelles.urban.dataimport.licences.importer import LicencesImporter
from imio.urban.dataimport.browser.adapter import ImporterFromSettingsForm
from imio.urban.dataimport.browser.import_panel import ImporterSettings


class LicencesImporterSettings(ImporterSettings):
    """
    """


class LicencesImporterFromImportSettings(ImporterFromSettingsForm):

    def __init__(self, settings_form, importer_class=LicencesImporter):
        """
        """
        super(LicencesImporterFromImportSettings, self).__init__(settings_form, importer_class)
