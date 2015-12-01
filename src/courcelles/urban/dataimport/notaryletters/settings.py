# -*- coding: utf-8 -*-

from courcelles.urban.dataimport.notaryletters.importer import NotarylettersImporter
from imio.urban.dataimport.browser.adapter import ImporterFromSettingsForm
from imio.urban.dataimport.browser.import_panel import ImporterSettings


class NotarylettersImporterSettings(ImporterSettings):
    """
    """


class NotarylettersImporterFromImportSettings(ImporterFromSettingsForm):

    def __init__(self, settings_form, importer_class=NotarylettersImporter):
        """
        """
        super(NotarylettersImporterFromImportSettings, self).__init__(settings_form, importer_class)
