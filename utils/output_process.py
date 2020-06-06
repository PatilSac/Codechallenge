import json
import os

from utils import search_books
from utils.xml_util import XMLUtil
from utils import logging


class OP:
    __s = object
    __byfield = {}
    log = logging.Logger.get_instance()


    @classmethod
    def process_output(cls):
        cls.__s = search_books.Search()

        cls.log.info('loading input.json')
        with open(os.path.dirname(os.getcwd()) + "/input.json") as f:
            data = json.load(f)

        year = data['year']

        cls.log.info('Calling search util and xml util functions')
        cls.__byfield = XMLUtil.get_book_name_byfield(cls.__s.search_by_field()[1])

        if year == "":
            cls.log.info('display results')
            OP.__display_output()
        else:
            cls.log.info('find match to the input YEAR and display results')
            OP.__find_match_and_display(year)

    @classmethod
    def __find_match_and_display(cls, year):
        n = 0
        if len(cls.__byfield) != 0:
            for k, v in cls.__byfield.items():
                if v[0] == year:
                    n += 1
                    print("AUTHOR NAME = \"{}\"     published year and title =     {}".format(k, ', '.join(map(str, v))))
        if n == 0:
            print("No Match")

    @classmethod
    def __display_output(cls):
        print(cls.__byfield)
        if len(cls.__byfield) != 0:
            for k, v in cls.__byfield.items():
                print("AUTHOR NAME = \"{}\"     published year and title =     {}".format(k, ', '.join(map(str, v))))
        else:
            print("No Match")


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
