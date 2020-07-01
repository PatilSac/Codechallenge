import pytest
from utils import logging

@pytest.fixture(scope="session", autouse=True)
def large_scope_fixtures():
    log = logging.Logger.get_instance()
    yield log

@pytest.fixture
def obj_search():
    from utils import search_books
    return search_books.Search()


@pytest.fixture
def xml_parse():
    from utils.xml_util import XMLUtil
    return XMLUtil
