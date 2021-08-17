from flask import url_for
from invenio_records.api import Record

from oarepo_records_draft.record import InvalidRecordAllowedMixin
from oarepo_references.mixins import ReferenceEnabledRecordMixin
from oarepo_validate import SchemaKeepingRecordMixin, MarshmallowValidatedRecordMixin

from .constants import THESES_ALLOWED_SCHEMAS, THESES_PREFERRED_SCHEMA, published_index_name
from .marshmallow import ThesisMetadataSchemaV2


class ThesisBaseRecord(SchemaKeepingRecordMixin,
                       MarshmallowValidatedRecordMixin,
                       ReferenceEnabledRecordMixin,
                       Record,
                       ):
    ALLOWED_SCHEMAS = THESES_ALLOWED_SCHEMAS
    PREFERRED_SCHEMA = THESES_PREFERRED_SCHEMA
    MARSHMALLOW_SCHEMA = ThesisMetadataSchemaV2


class PublishedThesisRecord(ThesisBaseRecord):
    index_name = published_index_name

    @property
    def canonical_url(self):
        return url_for('invenio_records_rest.thesis_item',
                       pid_value=self['control_number'],
                       _external=True)
