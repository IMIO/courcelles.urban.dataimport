# -*- coding: utf-8 -*-

from zope.interface import implements

from imio.urban.dataimport.access.importer import AccessDataImporter
from courcelles.urban.dataimport.interfaces import ICourcellesDataImporter


class CourcellesDataImporter(AccessDataImporter):
    """ """

    implements(ICourcellesDataImporter)
