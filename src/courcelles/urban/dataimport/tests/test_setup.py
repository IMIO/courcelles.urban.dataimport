# -*- coding: utf-8 -*-
"""Setup/installation tests for this package."""

from courcelles.urban.dataimport.testing import IntegrationTestCase
from plone import api


class TestInstall(IntegrationTestCase):
    """Test installation of courcelles.urban.dataimport into Plone."""

    def setUp(self):
        """Custom shared utility setup for tests."""
        self.portal = self.layer['portal']
        self.installer = api.portal.get_tool('portal_quickinstaller')

    def test_product_installed(self):
        """Test if courcelles.urban.dataimport is installed with portal_quickinstaller."""
        self.assertTrue(self.installer.isProductInstalled('courcelles.urban.dataimport'))

    def test_uninstall(self):
        """Test if courcelles.urban.dataimport is cleanly uninstalled."""
        self.installer.uninstallProducts(['courcelles.urban.dataimport'])
        self.assertFalse(self.installer.isProductInstalled('courcelles.urban.dataimport'))

    # browserlayer.xml
    def test_browserlayer(self):
        """Test that ICourcellesUrbanDataimportLayer is registered."""
        from courcelles.urban.dataimport.interfaces import ICourcellesUrbanDataimportLayer
        from plone.browserlayer import utils
        self.failUnless(ICourcellesUrbanDataimportLayer in utils.registered_layers())
