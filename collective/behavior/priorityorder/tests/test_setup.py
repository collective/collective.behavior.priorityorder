# -*- coding: utf-8 -*-
"""Setup/installation tests for this package."""

from collective.behavior.priorityorder.testing import IntegrationTestCase
from plone import api


class TestInstall(IntegrationTestCase):
    """Test installation of collective.behavior.priorityorder into Plone."""

    def setUp(self):
        """Custom shared utility setup for tests."""
        self.portal = self.layer['portal']
        self.installer = api.portal.get_tool('portal_quickinstaller')

    def test_product_installed(self):
        """Test if collective.behavior.talcondition is installed
        with portal_quickinstaller."""
        self.assertTrue(self.installer.isProductInstalled(
            'collective.behavior.priorityorder'))

    def test_uninstall(self):
        """Test if collective.behavior.priorityorder is cleanly uninstalled."""
        self.installer.uninstallProducts(['collective.behavior.priorityorder'])
        self.assertFalse(self.installer.isProductInstalled(
            'collective.behavior.priorityorder'))
