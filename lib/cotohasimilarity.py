import json
import os
import shutil

from lib.apicotoha import ApiCotoha
from lib.filewrapper import fw

class CotohaSimilarity():
    def __init__(self, clientId, clientSecret, __result_dir):
        self.__cotoha = ApiCotoha(clientId, clientSecret)

        self.__result_path = f'{__result_dir}\\similarity_data.txt'

    def exec(self, datas):
        similaritys = []
        for data in datas:
            if 'title' in data:
                similarity = self.__cotoha.similarity(data['title'], data['story'])
                if not similarity:
                    continue

                ret = {
                    'title' : data['title'],
                    'daily_point' : data['daily_point'],
                    'score' : similarity['score'],
                }

                similaritys.append(ret)

        fw.write(self.__result_path, similaritys)
