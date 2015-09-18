# -*- coding: utf-8 -*-
from plone import api

import logging


PROFILE_ID = 'profile-collective.behaviors.priorityorder:default'

def add_catalog_indexes(context, logger=None):
    """Method to add our wanted indexes to the portal_catalog.

    @parameters:

    When called from the import_various method below, 'context' is
    the plone site and 'logger' is the portal_setup logger.  But
    this method can also be used as upgrade step, in which case
    'context' will be portal_setup and 'logger' will be None.
    """
    if logger is None:
        # Called as upgrade step: define our own logger.
        logger = logging.getLogger(
            'collective.behaviors.priorityorder.setuphandlers')

    # Run the catalog.xml step as that may have defined new metadata
    # columns.  We could instead add <depends name="catalog"/> to
    # the registration of our import step in zcml, but doing it in
    # code makes this method usable as upgrade step as well.  Note that
    # this silently does nothing when there is no catalog.xml, so it

    # is quite safe.
    setup = api.portal.get_tool(name='portal_setup')
    setup.runImportStepFromProfile(PROFILE_ID, 'catalog')

    catalog = api.portal.get_tool(name='portal_catalog')
    indexes = catalog.indexes()
    # Specify the indexes you want, with ('index_name', 'index_type')
    wanted = (
        ('priority_order', 'FieldIndex'),
    )
    indexables = []
    for name, meta_type in wanted:
        if name not in indexes:
            catalog.addIndex(name, meta_type)
            indexables.append(name)
            logger.info("Added %s for field %s.", meta_type, name)
    # if len(indexables) > 0:
    #     logger.info("Indexing new indexes %s.", ', '.join(indexables))
    #     catalog.manage_reindexIndex(ids=indexables)
    indexables = [name for name, meta_type in wanted]
    logger.info("Indexing new indexes %s.", ', '.join(indexables))
    catalog.manage_reindexIndex(ids=indexables)


def importVarious(context):
    """Miscelaneous steps import handle
    """
    if context.readDataFile(
            'collective.behaviors.priorityorder_various.txt') is None:
        return
    logger = context.getLogger(
        'collective.behaviors.priorityorder.setuphandlers')
    portal = context.getSite()
    add_catalog_indexes(portal, logger)
