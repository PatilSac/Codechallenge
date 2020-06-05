import os

import pytest
import requests
import xml.etree.ElementTree as ET
import lxml.html as html



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
    assert bool(xml_parse.get_book_name_byyear(text))

def test_books_dir_xpath(obj_search):
    root = ET.fromstring(obj_search.search_by_field()[1])

    for node in root.findall('.//best_book/title'):
        log.info(node.text)

    for node in root.findall('.//best_book/author/name'):
        log.info(node.text)

    assert True

def test_books_byyear_xpath(obj_search):

    root = html.fromstring(obj_search.search_by_year()[1])

    for node in root.xpath('.//table/tr/td/div/a'):
        log.info(node)

    log.info('Done')
    assert True






