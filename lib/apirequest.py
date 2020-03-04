import json
import requests
import urllib

class ApiRequest():
    def __init__(self, url, method):
        self.__url = url
        self.__method = method
        self.__headers = {}
        self.__params = {}

    def addHeader(self, obj=None):
        self.__headers.update(obj)

    def addParam(self, obj=None):
        self.__params.update(obj)

    def throw(self):
        if self.__method == 'GET':
            url = '{}?{}'.format(self.__url, urllib.parse.urlencode(self.__params))
            res = requests.get(url=url, headers=self.__headers)
        if self.__method == 'POST':
            url = self.__url
            res = requests.post(url=url, headers=self.__headers, data=json.dumps(self.__params))

        if res.status_code != 200 and res.status_code != 201:
            print(f'url:{url}')
            print(f'status_code:{res.status_code}')
            print(f'header:{self.__headers}')
            print(f'param:{self.__params}')
            return False

        return res.json()
