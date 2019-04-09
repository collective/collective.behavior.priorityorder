# -*- coding: utf-8 -*-
from collective.behavior.priorityorder.testing import INTEGRATION_TESTING
from plone import api
from plone.app.testing import setRoles
from plone.app.testing import TEST_USER_ID

import unittest


class TestInstall(unittest.TestCase):
    """Test installation of collective.behavior.priorityorder into Plone."""
    layer = INTEGRATION_TESTING

    def setUp(self):
        """Custom shared utility setup for tests."""
        self.portal = self.layer['portal']
        setRoles(self.portal, TEST_USER_ID, ('Manager',))
        self.installer = api.portal.get_tool(name='portal_quickinstaller')

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
