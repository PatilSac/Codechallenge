import pytest


@pytest.fixture
def obj_search():
    from base import search_books
    return search_books.Search()
