import json
import os

from decouple import config
from utils.api_util import APIUtil
from utils.input_check import Validate
from utils import logging


class Search:

    def __init__(self):
        self.log = logging.Logger.get_instance()
        with open (os.path.dirname(os.getcwd())+"/input.json") as f:
            self.data = json.load(f)

        self.query, self.field, self.quote, self.year = Validate.validate_input(self.data)


    """
    Search books by field, author'\title or all
    returns response and xml content from the API
    """

    def search_by_field(self):

        payload = {
            'key': config('KEY'),
            'q': str(self.query),
            'search[field]': str(self.field)
        }
        """ payload creation can be separated in future """

        self.log.info('Payload created')

        response = APIUtil.get(url=config('SEARCH_URL'), params=payload)
        self.log.info('Search query hit')

        self.log.info('Response code is : ' + str(response['response']))

        self.log.info('Returning request data')

        return response['response'], response['text']


    def search_by_quote(self):

        payload = {
            'utf8': '✓',
            'q': str(self.quote),
            'commit': 'Search'
        }

        response = APIUtil.get(url=config('SEARCH_BY_QUOTE'), params=payload)

        self.log.info('Response code is : ' + str(response['response']))

        self.log.info('Returning request data')

        return response['response'], response['text']

    def search_by_year(self):

        year = str(self.year)

        if year is not None:
            response = APIUtil.get(url=config('SEARCH_BY_YEAR') + str(year))
        else:
            response = APIUtil.get(url=config('SEARCH_BY_YEAR'))

        self.log.info('Response code is : ' + str(response['response']))

        self.log.info('Returning request data')

        return response['response'], response['text']
