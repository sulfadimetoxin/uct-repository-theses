# -*- coding: utf-8 -*-
#
# This file is part of Invenio.
# Copyright (C) 2015-2018 CERN.
#
# Invenio is free software; you can redistribute it and/or modify it
# under the terms of the MIT License; see LICENSE file for more details.

"""Persistent identifier minters."""

from __future__ import absolute_import, print_function

from uct_repository_theses.providers import UCTRepositoryThesesIdProvider


def uct_repository_theses_pid_minter(record_uuid, data):
    """Mint loan identifiers."""
    assert 'control_number' in data
    provider = UCTRepositoryThesesIdProvider.create(
        object_type='rec',
        object_uuid=record_uuid,
        thesis_id=data['control_number']
    )
    return provider.pid
