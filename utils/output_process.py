import json
import os

from utils import search_books
from utils.xml_util import XMLUtil

class OP:
    __s = object
    __byfield = {}


    @classmethod
    def process_output(cls):
        cls.__s = search_books.Search()

        with open (os.path.dirname(os.getcwd())+"/input.json") as f:
            data = json.load(f)

        year = data['year']
        if year == "":
            OP.__display_output()
        else:
            cls.__byfield = XMLUtil.get_book_name_byfield(cls.__s.search_by_field()[1])
            OP.__find_match_and_display(year)


    @classmethod
    def __find_match_and_display(cls,year):
        for k, v in cls.__byfield:
            if v[0] == year:
                print("Author name = {} published year and title = {}".format(k, ', '.join(map(str, v))))


    @classmethod
    def __display_output(cls):
        for k,v in cls.__byfield:
            print("Author name = {} published year and title = {}".format(k,', '.join(map(str, v))))







    # def find_book_in_multiple_streams():
    #
    #     byyear = {}
    #     byquote = {}
    #     byfield = {}
    #
    #     s = search_books.Search()
    #
    #     byyear = XMLUtil.get_book_name_byyear(s.search_by_year()[1])
    #     byquote = XMLUtil.get_book_name_byquote(s.search_by_quote()[1])
    #     byfield = XMLUtil.get_book_name_byfield(s.search_by_field()[1])
    #
    #     print(byfield)
    #     print(byyear)
    #     print(byquote)
    #
    #     inter1 = byyear.keys() & byfield.keys() & byquote.keys()
    #     inter2 = byyear.keys() & byfield.keys()
    #     inter3 = byquote.keys() & byfield.keys()
    #     inter4 = byyear.keys() & byquote.keys()
    #
    #     print('Printing intersections 1')
    #     print(inter1)
    #
    #     print('Printing intersections 2')
    #     print(inter2)
    #
    #     print('Printing intersections 3')
    #     print(inter3)
    #
    #     print('Printing intersections 4')
    #     print(inter4)
