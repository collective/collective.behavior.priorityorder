# -*- coding: utf-8 -*-
from collective.behavior.priorityorder.testing import INTEGRATION_TESTING
from plone import api

import unittest


class TestBehavior(unittest.TestCase):
    layer = INTEGRATION_TESTING

    def setUp(self):
        """ """
        super(TestBehavior, self).setUp()
        portal = self.layer['portal']
        self.testitem1 = portal['testitem1']
        self.testitem2 = portal['testitem2']

    def test_behavior(self):
        self.testitem1.priority_order = 1
        self.testitem1.reindexObject()
        self.testitem2.priority_order = 2
        self.testitem2.reindexObject()

        catalog = api.portal.get_tool(name='portal_catalog')
        brains = catalog(sort_on='priority_order',
                         sort_order='ascending')

        self.assertEqual(brains[0].id, 'testitem1')

        self.testitem1.priority_order = 2
        self.testitem1.reindexObject()
        self.testitem2.priority_order = 1
        self.testitem2.reindexObject()
        brains = catalog(sort_on='priority_order',
                         sort_order='ascending')
        self.assertEqual(brains[0].id, 'testitem2')
