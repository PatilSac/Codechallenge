import requests
from urllib.error import HTTPError
from urllib.error import URLError

class API_Util:
    "Main base class for Requests based scripts"

    def __init__(self, url=None):
        pass


    def get(self, url,params=None,headers=None):
        "Util for Get request"
        if headers is None:
            headers = {}
        xml_response = None
        error = {}
        try:
            response = requests.get(url=url,headers=headers,params=params)
            try:
                xml_response = response.text
            except:
                xml_response = None
        except (HTTPError,URLError) as err:
            error = err
            if isinstance(err,HTTPError):
                error_message = err.read()
                print("Error in GET request : %s %s" % (url, error_message))
            else:
                print(err.reason.args)
                # bubble error back up after printing relevant details
                raise err # We raise error only when unknown errors occurs (other than HTTP error)

        return {'response': response.status_code,'text':response.text,'xml_response':xml_response, 'error': error}


    def post(self, url, params=None, data=None, json=None, headers=None):
        "Util for Post request"
        if headers is None:
            headers = {}
        error = {}
        xml_response = None
        try:
            response = requests.post(url,params=params,json=json,headers=headers)
            try:
                xml_response = response.text
            except:
                xml_response = None
        except (HTTPError,URLError) as err:
            error = err
            if isinstance(err, HTTPError):
                error_message = err.read()
                print("Error in POST request : %s %s" % (url, error_message))
            else:
                print(err.reason.args)
                raise err  # We raise error only when unknown errors occurs (other than HTTP error)

        return {'response': response.status_code, 'text': response.text, 'xml_response': xml_response, 'error': error}

