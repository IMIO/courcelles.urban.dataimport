# -*- coding: utf-8 -*-

from courcelles.urban.dataimport.architects.importer import ArchitectsImporter
from imio.urban.dataimport.browser.controlpanel import ImporterControlPanel
from imio.urban.dataimport.browser.import_panel import ImporterSettings
from imio.urban.dataimport.browser.import_panel import ImporterSettingsForm
from imio.urban.dataimport.acropole.settings import AcropoleImporterFromImportSettings
from imio.urban.dataimport.csv.settings import CSVImporterFromImportSettings


class CourcellesImporterSettingsForm(ImporterSettingsForm):
    """ """


class CourcellesImporterSettings(ImporterSettings):
    """ """
    form = CourcellesImporterSettingsForm


class CourcellesImporterControlPanel(ImporterControlPanel):
    """ """
    import_form = CourcellesImporterSettings


class LicencesImporterFromImportSettings(AcropoleImporterFromImportSettings):
    """ """

    def get_importer_settings(self):
        """
        Return the db name to read.
        """
        settings = super(LicencesImporterFromImportSettings, self).get_importer_settings()

        db_settings = {
            'db_name': 'urb64015ac',
        }

        settings.update(db_settings)

        return settings


class ArchitectsImporterFromImportSettings(CSVImporterFromImportSettings):
    """ """

    def __init__(self, settings_form, importer_class=ArchitectsImporter):
        """
        """
        super(CSVImporterFromImportSettings, self).__init__(settings_form, importer_class)

    def get_importer_settings(self):
        """
        Return the csv file to read.
        """
        settings = super(ArchitectsImporterFromImportSettings, self).get_importer_settings()

        csv_settings = {
            'csv_filename': 'Architectes.csv',
            'key_column': 'nom',
        }

        settings.update(csv_settings)

        return settings
