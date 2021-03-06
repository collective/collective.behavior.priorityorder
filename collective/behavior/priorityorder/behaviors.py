# -*- coding: utf-8 -*-
from collective.behavior.priorityorder import _
from plone.autoform.interfaces import IFormFieldProvider
from plone.supermodel import model
from zope import schema
from zope.interface import alsoProvides


class IPriorityOrdering(model.Schema):
    """Add a ordering field"""

    priority_order = schema.Int(
        title=_(u"Priority Order"),
        description=_(u"Enter a number for setting the priority. "
                      u"Highest priority = 1"),
        required=False,
        default=1000,
    )

alsoProvides(IPriorityOrdering, IFormFieldProvider)
