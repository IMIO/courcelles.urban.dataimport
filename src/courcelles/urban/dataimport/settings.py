# -*- coding: utf-8 -*-

from imio.urban.dataimport.browser.controlpanel import ImporterControlPanel
from imio.urban.dataimport.browser.import_panel import ImporterSettings
from imio.urban.dataimport.browser.import_panel import ImporterSettingsForm
from imio.urban.dataimport.access.settings import AccessImporterFromImportSettings


class CourcellesImporterSettingsForm(ImporterSettingsForm):
    """ """

class CourcellesImporterSettings(ImporterSettings):
    """ """
    form = CourcellesImporterSettingsForm


class CourcellesImporterControlPanel(ImporterControlPanel):
    """ """
    import_form = CourcellesImporterSettings


class CourcellesImporterFromImportSettings(AccessImporterFromImportSettings):
    """ """

    def get_importer_settings(self):
        """
        Return the db name to read.
        """
        settings = super(CourcellesImporterFromImportSettings, self).get_importer_settings()

        db_settings = {
            'db_name': '',
        }

        settings.update(db_settings)

        return settings
