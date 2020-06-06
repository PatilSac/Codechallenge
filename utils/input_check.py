
class Validate:

    @staticmethod
    def validate_input(data):

        query = (data['query'][:50]) if len(data) > 75 else data

        field = (data['field'][:50]) if len(data) > 75 else data



        return query, field, quote, year

