import json
import os

from decouple import config
from utils.api_util import APIUtil
from utils.input_check import Validate
from utils import logging

class Search:

    def __init__(self):
        self.__query = ""
        self.__field = ""
        self.__quote = ""
        self.__year = ""
        self.__log = logging.Logger.get_instance()

        with open (os.path.dirname(os.getcwd())+"/input.json") as f:
            self.__data = json.load(f)

        self.__query, self.__field, self.__quote, self.__year = Validate._validate_input(self.__data)


    """
    Search books by field, author'\title or all
    returns response and xml content from the API
    """

    def search_by_field(self):

        payload = {
            'key': config('KEY'),
            'q': str(self.__query),
            'search[field]': str(self.__field)
        }
        """ payload creation can be separated in future """

        self.__log.info('Payload created')

        response = APIUtil.get(url=config('SEARCH_URL'), params=payload)
        self.__log.info('Search query hit')

        self.__log.info('Response code is : ' + str(response['response']))

        self.__log.info('Returning request data')

        return response['response'], response['text']


    def search_by_quote(self):

        payload = {
            'utf8': '✓',
            'q': str(self.__quote),
            'commit': 'Search'
        }

        response = APIUtil.get(url=config('SEARCH_BY_QUOTE'), params=payload)

        self.__log.info('Response code is : ' + str(response['response']))

        self.__log.info('Returning request data')

        return response['response'], response['text']

    def search_by_year(self):

        year = str(self.__year)

        if year is not None:
            response = APIUtil.get(url=config('SEARCH_BY_YEAR') + str(year))
        else:
            response = APIUtil.get(url=config('SEARCH_BY_YEAR'))

        self.__log.info('Response code is : ' + str(response['response']))

        self.__log.info('Returning request data')

        return response['response'], response['text']
