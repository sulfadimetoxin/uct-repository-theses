from invenio_search import RecordsSearch


class ThesisRecordSearch(RecordsSearch):
    LIST_SOURCE_FIELDS = [
        'control_number',
        'title', 'dateIssued', 'creator', 'resourceType',
        'contributor', 'keywords', 'subject', 'abstract', 'state', 'accessRights',
        'language',
        '$schema'
    ]
    HIGHLIGHT_FIELDS = {
        'title.cs': None,
        'title._': None,
        'title.en': None
    }