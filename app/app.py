from . import base_file

class App(base_file):

    def find_book(self):
        print('Finding book for data in input.json')
        base_file.predefined.output_process.search_books.config()














if __name__ == "__main__":
    find_book()