import os
import inspect

from lib.apirequest import ApiRequest

class ApiCotoha():
    def __init__(self, clientId, clientSecret):
        self.__clientId = clientId
        self.__clientSecret = clientSecret

    def __access(self):
        at = ApiRequest('https://api.ce-cotoha.com/v1/oauth/accesstokens', 'POST')
        at.addHeader({'Content-Type':'application/json'})
        at.addParam({
            'grantType': 'client_credentials',
            'clientId': self.__clientId,
            'clientSecret': self.__clientSecret,
        })

        res = at.throw()
        if not res:
            print('cotoha auth is failed')
            exit(1)

        return res['access_token']

    def __common(self, param):
        target = inspect.currentframe().f_back.f_code.co_name
        ar = ApiRequest(f'https://api.ce-cotoha.com/api/dev/nlp/v1/{target}', 'POST')
        ar.addHeader({
            'Content-Type' : 'application/json;charset=UTF-8',
            'Authorization' :  f"Bearer {self.__access()}",
        })
        ar.addParam(param)

        res = ar.throw()
        if not res:
            return False

        if res['status'] != 0:
            print(f'status:{res["status"]}')
            print(f'message:{res["message"]}')
            return False

        return res['result']

    def keyword(self, document):
        return self.__common(
            {
                'document': document,
                'type' : 'kuzure',
                'max_keyword_num' : 10,
            }
        )

    def similarity(self, s1, s2):
        return self.__common(
            {
                's1': s1,
                's2': s2,
                'type' : 'kuzure',
            }
        )

