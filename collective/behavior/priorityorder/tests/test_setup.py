# -*- coding: utf-8 -*-
from collective.behavior.priorityorder import PROJECT_NAME
from collective.behavior.priorityorder.testing import INTEGRATION_TESTING
from plone import api
from Products.CMFPlone.utils import get_installer

import unittest


class TestInstall(unittest.TestCase):
    """Test installation of collective.behavior.priorityorder into Plone."""
    layer = INTEGRATION_TESTING

    def setUp(self):
        """Custom shared utility setup for tests."""
        self.portal = self.layer['portal']
        self.qi = get_installer(self.portal)

    def test_product_installed(self):
        """Test if collective.behavior.talcondition is installed
        with portal_quickinstaller."""
        self.assertTrue(self.qi.is_product_installed(
            PROJECT_NAME), 'package appears not to have been installed')

    def test_uninstall(self):
        """Test if collective.behavior.priorityorder is cleanly uninstalled."""
        self.qi.uninstall_product(PROJECT_NAME)
        self.assertFalse(self.qi.is_product_installed(
            PROJECT_NAME))
