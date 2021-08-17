import os

THESES_ALLOWED_SCHEMAS = ['uct_repository_theses/uct-repository-theses-v1.0.0.json']
THESES_PREFERRED_SCHEMA = 'uct_repository_theses/uct-repository-theses-v1.0.0.json'


PUBLISHED_THESIS_PID_TYPE = 'thesis'
PUBLISHED_THESIS_RECORD = 'uct_repository_theses.record:PublishedThesisRecord'


published_index_name = 'uct_repository_theses-uct-repository-theses-v1.0.0'


prefixed_published_index_name = os.environ.get('INVENIO_SEARCH_INDEX_PREFIX',
                                               '') + published_index_name
