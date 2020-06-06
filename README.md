# Codechallenge

This is a CodeChallenge, app.py runs and consumes input.json file updated by user in the root folder, books searched are displayed on the console. 
Note: Output can be modified to be a json or another type of file in future.


## Prerequisites

Ensure that you have Python 3.7.*

project setup:

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
|   |-- log_07_06_2020__01:59.log
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
|-- .env                            ---------------------   .env file with constants read by python-decouple
|-- input.json                      ---------------------   user enter input in json here
|-- report.html                     ---------------------   unit test html report
|-- requirements.txt                ---------------------   project requirements

```

1. Ensure that you have docker, docker-compose installed
```
sudo apt-get update
sudo apt-get install docker-ce
sudo apt-get install docker-compose
```
2. Clone git repo
```
git clone https://github.com/PatilSac/django_quiz.git
```
3. Build the services written in docker_compose
```
docker-compose -f docker-compose.yml build
```
4. Run the services using docker_compose
```
docker-compose -f docker-compose.yml up
```

## Containers

There are two servers. Dockerfiles for them are located at:
django_server : docker_compose/docker/Dockerfile
nginx_server  : docker_compose/nginx/Dockerfile


### Network

## Gunicorn
Python Web Server Gateway Interface HTTP server, running at 0.0.0.0:8000 in the django_server container. This is something that executes Python as Python isn't the best at handling all types of requests.

## Nginx
Web server, reverse proxy, load balancer, mail proxy and HTTP cache combination being used here for django rest framework. It is running at port 80 in its docker container and serving Gunicorn.

### CI/CD
