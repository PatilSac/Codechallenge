class Validate:

    @staticmethod
    def validate_input(data):
        query = (data['query'][:50]) if len(data['query']) > 50 else data['query']

        field = (data['field']) if str(data['field']).lower() == "author" or str(
            data['field']).lower() == "title" else "all "

        quote = (data['quote'][:50]) if len(data['quote']) > 50 else data['quote']

        year = (data['year']) if int(data['year']) > 0 else ""

        return query, field, quote, year
