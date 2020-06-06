import os
import xml.etree.ElementTree as ET
from utils import logging
from decouple import config
import lxml.html as html

class XMLUtil:
    "Main class for xml based scripts related to this challenge"

    log = logging.Logger.get_instance()
    book = {}

    @classmethod
    def get_book_name_byfield(cls,file):

        root = ET.fromstring(file)
        author = []
        title = []
        year = []

        for node in root.findall(config('XPATH_TITLE')):
            # cls.log.info(node.text)
            title.append(node.text)

        for node in root.findall(config('XPATH_AUTHOR')):
            # cls.log.info(node.text)
            author.append(node.text)

        for node in root.findall(config('XPATH_YEAR')):
            if node.text is not None:
                year.append(node.text)
            else:
                year.append("")

        temp = {key: value for (key, value) in zip(author, year)}

        temp2 = {key: value for (key, value) in zip(author, title)}

        # print(temp.keys())
        # print(zip(temp.values(), temp2.values()))
        #
        # cls.book = { i:list(j) for i in temp.keys() for j in zip(temp.values(), temp2.values())}

        ds = [temp, temp2]

        for k in temp.keys():
            cls.book[k] = tuple(d[k] for d in ds)

        return cls.book


    @classmethod
    def get_book_name_byyear(cls, file):

        author = []
        title = []
        root = html.fromstring(file)

        for node in root.xpath(config('XPATH_YEAR_TITLE')):
            title.append(node.text_content())

        for node in root.xpath(config('XPATH_YEAR_AUTHOR')):
            author.append(node.text_content())

        cls.book = {key: value for (key, value) in zip(author, title)}

        return cls.book

    @classmethod
    def get_book_name_byquote(cls, file):

        author = []
        title = []
        root = html.fromstring(file)

        for node in root.xpath(config('XPATH_QUOTE_TITLE')):
            title.append(node.text_content())

        for node in root.xpath(config('XPATH_QUOTE_AUTHOR')):
            author.append(node.text_content())

        cls.book = {key: value for (key, value) in zip(author, title)}

        return cls.book





    """
        OLD METHOD NEED be commented out or removed, kept for reference.
    """
    def _get_book_name_byfield(cls,file):
        #tree = et.ElementTree(file=os.path.dirname(os.getcwd()) + "/ignore/" + "byfield.xml")
        cls.log.info('in get_book method')

        with open (os.path.dirname(os.getcwd()) + "/ignore/" + "byfield.xml",'w+') as xml_file:
            xml_file.write(file)
        cls.log.info('xml file created')

        tree = ET.parse(os.path.dirname(os.getcwd()) + "/ignore/" + "byfield.xml")

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

    """
        old method can be commented out or removed, kept for reference.
    """
    def _get_book_name_byyear(cls, file):

        cls.log.info('in get_book_name_byyear method')
        with open(os.path.dirname(os.getcwd()) + "/ignore/" + "byyear.html", 'w+') as xml_file:
            xml_file.write(file)
        cls.log.info('xml file created')

        tree = ET.parse(os.path.dirname(os.getcwd()) + "/ignore/" + "byyear.html")

        cls.log.info('tree object created')
        root = tree.getroot()
        cls.log.info(list(root))


