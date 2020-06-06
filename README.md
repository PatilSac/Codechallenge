# Codechallenge

This is a dockerized django rest framework example. Once docker-compose is UP, there will be two services running based on own Dockerfiles sitting in the docker_compose directory. App code is in app folder. 

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
|   |-- app.py
|
|-- base/
|   |-- get_accesstoken.py
|   |-- predefined.py
|
|-- logs/
|   |-- log_07_06_2020__01:51.log
|   |-- log_07_06_2020__01:59.log
|
|-- test/
|   |-- conftest.py
|   |-- test_search_books.py
|
|-- utils/
|   |-- logging.py
|   |-- api_util.py
|   |-- xml_util.py
|   |-- input_check.py
|   |-- output_process.py
|   |-- search_books.py
|
|-- .env
|-- input.json
|-- report.html
|-- requirements.txt

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
