import requests
from urllib.error import HTTPError
from urllib.error import URLError


class APIUtil:
    "Main base class for Requests based scripts"

    @staticmethod
    def get(url, headers=None):
        "Util for Get request"
        if headers is None:
            headers = {}
        json_response = None
        response = False
        error = {}
        try:
            response = requests.get(url=url, headers=headers, params=params)
            try:
                json_response = response.json()
            except:
                json_response = None
        except (HTTPError, URLError) as err:
            error = err
            if isinstance(err, HTTPError):
                error_message = err.read()
                print("Error in GET request : %s %s" % (url, error_message))
            else:
                print(err.reason.args)
                # bubble error back up after printing relevant details
                raise err  # We raise error only when unknown errors occurs (other than HTTP error)

        return {'response': response.status_code, 'text': response.text, 'json_response': json_response, 'error': error}


    @staticmethod
    def post(url, params=None, data=None, json=None, headers=None):
        "Util for Post request"
        if headers is None:
            headers = {}
        error = {}
        response = False
        json_response = None
        try:
            response = requests.post(url, params=params, json=json, headers=headers)
            try:
                json_response = response.json()
            except:
                json_response = None
        except (HTTPError, URLError) as err:
            error = err
            if isinstance(err, HTTPError):
                error_message = err.read()
                print("Error in POST request : %s %s" % (url, error_message))
            else:
                print(err.reason.args)
                raise err  # We raise error only when unknown errors occurs (other than HTTP error)

        return {'response': response.status_code, 'text': response.text, 'json_response': json_response, 'error': error}

    @staticmethod
    def delete(url,headers=None):
        "Delete request"
        response = False
        json_response = None
        if headers is None:
            headers = {}
        error = {}

        try:
            response = requests.delete(url,headers = headers)
            try:
                json_response = response.json()
            except:
                json_response = None

        except (HTTPError,URLError) as err:
            error = err
            if isinstance(err, HTTPError):
                error_message = err.read()
                print("Error in DELETE request : %s %s" % (url, error_message))
            else:
                print(err.reason.args)
                raise err  # We raise error only when unknown errors occurs (other than HTTP error)

        return {'response': response.status_code,'text':response.text,'json_response':json_response, 'error': error}

    @staticmethod
    def put(url,json=None, headers=None):
        "Put request"
        error = {}
        response = False
        json_response = None

        try:
            response = requests.put(url,json=json,headers=headers)
            try:
                json_response = response.json()
            except:
                json_response = None

        except (HTTPError, URLError) as err:

            error = err
            if isinstance(err, HTTPError):
                error_message = err.read()
                print("Error in PUT request : %s %s" % (url, error_message))
            else:
                print(err.reason.args)
                raise err  # We raise error only when unknown errors occurs (other than HTTP error)

        return {'response': response.status_code, 'text': response.text, 'json_response': json_response, 'error': error}

