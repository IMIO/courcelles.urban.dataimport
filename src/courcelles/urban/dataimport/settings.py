# -*- coding: utf-8 -*-

from imio.urban.dataimport.browser.controlpanel import ImporterControlPanel
from imio.urban.dataimport.browser.import_panel import ImporterSettings
from imio.urban.dataimport.browser.import_panel import ImporterSettingsForm


class CourcellesImporterSettingsForm(ImporterSettingsForm):
    """ """


class CourcellesImporterSettings(ImporterSettings):
    """ """
    form = CourcellesImporterSettingsForm


class CourcellesImporterControlPanel(ImporterControlPanel):
    """ """
    import_form = CourcellesImporterSettings
