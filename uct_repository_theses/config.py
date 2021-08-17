# -*- coding: utf-8 -*-
#
# Copyright (C) 2019 CERN.
#
# My site is free software; you can redistribute it and/or modify it under
# the terms of the MIT License; see LICENSE file for more details.

"""Default configuration."""

from __future__ import absolute_import, print_function

from invenio_indexer.api import RecordIndexer
from invenio_records_rest.utils import allow_all, check_elasticsearch, deny_all
from invenio_search import RecordsSearch


from uct_repository_theses.constants import PUBLISHED_THESIS_PID_TYPE, PUBLISHED_THESIS_RECORD, published_index_name


def _(x):
    """Identity function for string extraction."""
    return x


RECORDS_REST_ENDPOINTS = {
    'thesis': dict(
        pid_type=PUBLISHED_THESIS_PID_TYPE,
        pid_minter='uct_repository_theses',
        pid_fetcher='uct_repository_theses',
        default_endpoint_prefix=True,
        record_class=PUBLISHED_THESIS_RECORD,
        search_class=RecordsSearch,
        indexer_class=RecordIndexer,
        search_index=published_index_name,
        search_type=None,
        record_serializers={
            'application/json': 'oarepo_validate:json_response',
        },
        search_serializers={
            'application/json': 'oarepo_validate:json_search',
        },
        list_route='/theses/',
        item_route='/theses/<pid(PUBLISHED_THESIS_PID_TYPE):pid_value>',
        default_media_type='application/json',
        max_result_window=10000,
        error_handlers=dict(),
        create_permission_factory_imp=allow_all,
        read_permission_factory_imp=allow_all,
        update_permission_factory_imp=deny_all,
        delete_permission_factory_imp=deny_all,
        list_permission_factory_imp=allow_all
    ),
}
"""REST API for my-site."""


RECORDS_REST_SORT_OPTIONS = dict(
    published_index_name=dict(
        bestmatch=dict(
            title=_('Best match'),
            fields=['_score'],
            default_order='desc',
            order=1,
        ),
        mostrecent=dict(
            title=_('Most recent'),
            fields=['-_created'],
            default_order='asc',
            order=2,
        ),
    )
)
"""Setup sorting options."""


RECORDS_REST_DEFAULT_SORT = dict(
    published_index_name=dict(
        query='bestmatch',
        noquery='mostrecent',
    )
)
"""Set default sorting options."""
