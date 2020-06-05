import os
import xml.etree.ElementTree as et
from utils import logging


class XMLUtil:
    "Main class for xml based scripts related to this challenge"

    log = logging.Logger.get_instance()
    book = {}

    @classmethod
    def get_book_name_byfield(cls,file):
        #tree = et.ElementTree(file=os.path.dirname(os.getcwd()) + "/ignore/" + "byfield.xml")
        cls.log.info('in get_book method')

        with open (os.path.dirname(os.getcwd()) + "/ignore/" + "byfield.xml",'w+') as xml_file:
            xml_file.write(file)
        cls.log.info('xml file created')

        tree = et.parse(os.path.dirname(os.getcwd()) + "/ignore/" + "byfield.xml")

        cls.log.info('tree object created')

        root = tree.getroot()

        cls.log.info('root object created')

        book_elements = list(list(root)[1][6])

        cls.log.info('Book element object created, location can be changed if xml changes')

        author = [(list(book_elements[i][8][2])[1]).text for i in range(0,len(book_elements))]
        title = [(book_elements[i][8][1]).text for i in range(0,len(book_elements))]
        cls.log.info('Created author and title list')

        cls.book = {key: value for (key, value) in zip(author, title)}

        return cls.book

    @classmethod
    def get_book_name_byyear(cls, file):

        cls.log.info('in get_book_name_byyear method')
        with open(os.path.dirname(os.getcwd()) + "/ignore/" + "byyear.html", 'w+') as xml_file:
            xml_file.write(file)
        cls.log.info('xml file created')

        tree = et.parse(os.path.dirname(os.getcwd()) + "/ignore/" + "byyear.html")

        cls.log.info('tree object created')
        root = tree.getroot()
        cls.log.info(list(root))







