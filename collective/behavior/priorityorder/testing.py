# -*- coding: utf-8 -*-
"""Base module for unittesting."""

from plone.app.robotframework.testing import AUTOLOGIN_LIBRARY_FIXTURE
from plone.app.testing import applyProfile
from plone.app.testing import FunctionalTesting
from plone.app.testing import IntegrationTesting
from plone.app.testing import login
from plone.app.testing import PLONE_FIXTURE
from plone.app.testing import PloneSandboxLayer
from plone.app.testing import setRoles
from plone.app.testing import TEST_USER_ID
from plone.app.testing import TEST_USER_NAME
from plone.testing import z2

import collective.behavior.priorityorder
import unittest2 as unittest


class CollectiveBehaviorPriorityOrderLayer(PloneSandboxLayer):

    defaultBases = (PLONE_FIXTURE,)
    products = ('collective.behavior.priorityorder',)

    def setUpZope(self, app, configurationContext):
        """Set up Zope."""
        # Load ZCML
        import plone.app.dexterity
        self.loadZCML(package=plone.app.dexterity)
        self.loadZCML(package=collective.behavior.priorityorder,
                      name='testing.zcml')
        for p in self.products:
            z2.installProduct(app, p)

    def setUpPloneSite(self, portal):
        """Set up Plone."""
        applyProfile(portal, 'plone.app.dexterity:default')
        #applyProfile(portal, 'Products.CMFPlone:plone-content')
        # Install into Plone site using portal_setup
        applyProfile(portal, 'collective.behavior.priorityorder:testing')

        # Login and create some test content
        setRoles(portal, TEST_USER_ID, ['Manager'])
        login(portal, TEST_USER_NAME)
        portal.invokeFactory(id='testitem1',
                             type_name='testtype',
                             title='Test type')
        self.testitem1 = portal.testitem1
        portal.invokeFactory(id='testitem2',
                             type_name='testtype',
                             title='Test type')
        self.testitem2 = portal.testitem2

        # Commit so that the test browser sees these objects
        import transaction
        transaction.commit()

    def tearDownZope(self, app):
        """Tear down Zope."""
        for p in reversed(self.products):
            z2.uninstallProduct(app, p)


FIXTURE = CollectiveBehaviorPriorityOrderLayer(
    name="FIXTURE"
    )


INTEGRATION = IntegrationTesting(
    bases=(FIXTURE,),
    name="INTEGRATION"
    )


FUNCTIONAL = FunctionalTesting(
    bases=(FIXTURE,),
    name="FUNCTIONAL"
    )


ACCEPTANCE = FunctionalTesting(bases=(FIXTURE,
                                      AUTOLOGIN_LIBRARY_FIXTURE,
                                      z2.ZSERVER_FIXTURE),
                               name="ACCEPTANCE")


class IntegrationTestCase(unittest.TestCase):
    """Base class for integration tests."""

    layer = INTEGRATION

    def setUp(self):
        super(IntegrationTestCase, self).setUp()
        self.portal = self.layer['portal']


class FunctionalTestCase(unittest.TestCase):
    """Base class for functional tests."""

    layer = FUNCTIONAL
