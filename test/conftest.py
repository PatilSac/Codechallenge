import pytest


@pytest.fixture
def obj_search():
    from base import search_books
    return search_books.Search()


@pytest.fixture
def xml_parse():
    from utils.xml_util import XMLUtil
    return XMLUtil
