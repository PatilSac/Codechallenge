import xml.etree.ElementTree as ET
import lxml.html as html
from decouple import config



from utils import logging

log = logging.Logger.get_instance()


def test_search_by_field_statustest(obj_search):
    code,text = obj_search.search_by_field()
    assert code == 200

def test_search_by_field_output(obj_search, xml_parse):
    code,text = obj_search.search_by_field()
    books = xml_parse.get_book_name_byfield(text)
    assert bool(books)
    log.info(books)

def test_books_byyear_statustest(obj_search):
    code,text = obj_search.search_by_year()
    assert code == 200


def test_books_byyear_output(obj_search, xml_parse):
    code,text = obj_search.search_by_year()
    books = xml_parse.get_book_name_byyear(text)
    assert bool(books)
    log.info(books)


def test_books_byquote_statustest(obj_search):
    code, text = obj_search.search_by_quote()
    assert code == 200

def test_books_byquote_output(obj_search,xml_parse):
    code, text = obj_search.search_by_quote()
    books = xml_parse.get_book_name_byquote(text)
    assert bool(books)
    log.info(books)





# def test_books_dir_xpath(obj_search,xml_parse):
#     root = html.fromstring(obj_search.search_by_year()[1])
#     author = []
#     title = []
#
#     for node in root.xpath(config('XPATH_YEAR_TITLE')):
#         title.append(node.text_content())
#
#     for node in root.xpath(config('XPATH_YEAR_AUTHOR')):
#         author.append(node.text_content())
#
#     log.info({key: value for (key, value) in zip(author, title)})
#
#
#
# def test_books_dir_xpath(obj_search,xml_parse):
#     code,text = obj_search.
#
#     root = ET.fromstring(obj_search.search_by_field()[1])
#     author = []
#     title = []
#
#     for node in root.findall(config('XPATH_TITLE')):
#         # cls.log.info(node.text)
#         title.append(node.text)
#
#     for node in root.findall(config('XPATH_AUTHOR')):
#         # cls.log.info(node.text)
#         author.append(node.text)
#
#     log.info({key: value for (key, value) in zip(author, title)})
#
# def test_books_byyear_xpath(obj_search):
#     root = html.fromstring(obj_search.search_by_year()[1])
#     author = []
#     title = []
#
#     for node in root.xpath(config('XPATH_YEAR_TITLE')):
#         title.append(node.text_content())
#
#     for node in root.xpath(config('XPATH_YEAR_AUTHOR')):
#         author.append(node.text_content())
#
#     log.info({key: value for (key, value) in zip(author, title)})
#
