# -*- coding: utf-8 -*-

from courcelles.urban.dataimport.notaries.importer import NotariesImporter
from imio.urban.dataimport.access.settings import AccessImporterFromImportSettings


class NotariesImporterFromImportSettings(AccessImporterFromImportSettings):
    """ """

    def __init__(self, settings_form, importer_class=NotariesImporter):
        """
        """
        super(AccessImporterFromImportSettings, self).__init__(settings_form, importer_class)

    def get_importer_settings(self):
        """
        Return the mdb file to read.
        """
        settings = super(NotariesImporterFromImportSettings, self).get_importer_settings()

        db_settings = {
            'db_name': 'registre_data.mdb',
            'table_name': 'adressenotaires',
            'key_column': 'NOM',
        }

        settings.update(db_settings)

        return settings
