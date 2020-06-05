import pytest
import requests

from utils import logging

log = logging.Logger.get_instance()


def test_search_by_field_statustest(obj_search):
    code,text = obj_search.search_by_field()
    assert code == 200


def test_books_dictionary(obj_search, xml_parse):
    code,text = obj_search.search_by_field()
    assert bool(xml_parse.get_book_name_byfield(text))


def test_books_byyear_statustest(obj_search):
    code,text = obj_search.search_by_year()
    assert code == 200


def test_books_byyear_dictionary(obj_search, xml_parse):
    code,text = obj_search.search_by_year()
    assert code == 200



