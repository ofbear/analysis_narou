import json
import os

from lib.apirequest import ApiRequest
from lib.filewrapper import fw

class ApiNarou(ApiRequest):
    def __init__(self, obj, reload=False, path=""):
        if reload or not os.path.isfile(path):
            super().__init__('https://api.syosetu.com/novelapi/api/', 'GET')
            super().addParam(obj=obj)
            res = super().throw()
            if not res:
                print('getting narou data is failed')
                exit(1)

            fw.write(path, res)
        
        self.__data = fw.read(path)

    @property
    def data(self):
        return self.__data
       
