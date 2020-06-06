from utils import logging


class Validate:
    log = logging.Logger.get_instance()

    @classmethod
    def validate_input(cls,data):

        cls.log.info('Checking query string provided in input JSON')
        query = (data['query'][:50]) if len(data['query']) > 50 else data['query']

        cls.log.info('Checking field string provided in input JSON')
        field = (data['field']) if str(data['field']).lower() == "author" or str(
            data['field']).lower() == "title" else "all"

        cls.log.info('Checking quote provided in input JSON')
        quote = (data['quote'][:50]) if len(data['quote']) > 50 else data['quote']

        cls.log.info('Checking if the year provided is less than 0')

        if data['year'] != "" or not type(int(data['year'])) is int:
            raise TypeError("Only integers are allowed in Year")
        elif int(data['year']) <= 0:
            raise ValueError("Year value should be more than 0")

        year = data['year']

        return query, field, quote, year
