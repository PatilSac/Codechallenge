# Codechallenge

This is a CodeChallenge, app.py runs and consumes input.json file updated by user in the root folder, books searched are displayed on the console. 

Note: 
- Output can be modified to be a json or another type of file in future.
- Out of requirements of the challenge program currently searches books based on author name, book title, year only due to limitations of goodreads api limits.
- Need to improve understanding of api methods for other challenge requirements

### Prerequisites

Ensure that you have Python 3.7.*

project setup: (replace with appropriate commands)

```
git clone https://github.com/PatilSac/Codechallenge.git
cd \path\to\project
pip3 install -r requirements.txt
```

### Getting Started

Project structure

```
Project/
|-- app/
|   |-- app.py                      ---------------------   Program execution starts from here
|
|-- base/
|   |-- predefined.py               ---------------------   Startup class file initilizes the process
|
|-- logs/
|   |-- log_07_06_2020__01:51.log   ---------------------   unit test logs here
|
|-- test/
|   |-- conftest.py                 ---------------------   conftest holds pytest fixure methods for tests
|   |-- test_search_books.py        ---------------------   unit test methods here
|
|-- utils/
|   |-- logging.py                  ---------------------   singleton logging infrastructure
|   |-- api_util.py                 ---------------------   public CRUD api methods
|   |-- xml_util.py                 ---------------------   xml parsing methods for different input fields
|   |-- input_check.py              ---------------------   input json file validation methods
|   |-- output_process.py           ---------------------   output process method
|   |-- search_books.py             ---------------------   search methods by different fields
|
|-- .env                            ---------------------   .env with constants read by python-decouple
|-- input.json                      ---------------------   user enter input in json here
|-- report.html                     ---------------------   unit test html report
|-- requirements.txt                ---------------------   project requirements

```
### Postman collection

https://www.getpostman.com/collections/458423a792cd7c0cce14

Steps:
1. goto GET request 'auth' 
2. get developer key from goodreads and put it in environment variables in postman
3. ensure that key is set to {{key}} to fetch it from environment variables.
4. update the headers as per requirement
5. check response

### Program run

Steps:
1. Update proper values in input.json with the fields for the book to search
```
{
  "query": "airforce",              ---------------------   test to search
  "field": "title",                 ---------------------   type of above text, either author/title/all
  "quote": "",                      ---------------------   quote (currently output process not setup)
  "year": "1997"                    ---------------------   year of publish book
}
```
2. Goto terminal and do following
```
cd /path/to/project root
python3 app/app.py 
```
3. Observe output on terminal


### Unit test

|-- test/ has uni tests.

conftest.py defines pytest fixtures, which acts as pre test setup for tests in 
other test_*.py files in the directory

Steps to run: (replace with appropriate commands)
```
cd /path/to/test_folder
py.test <test_class>.py --html=report.html
```
