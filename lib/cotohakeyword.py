import json
import os
import shutil

from lib.apicotoha import ApiCotoha
from lib.filewrapper import fw

class CotohaKeyword():
    def __init__(self, clientId, clientSecret, __result_dir):
        self.__cotoha = ApiCotoha(clientId, clientSecret)

        self.__result_path = f'{__result_dir}\\keyword_data.txt'

    def exec(self, datas):
        keywords = self.__extraKeyWord(datas)

        counts = self.__countKeyWord(keywords)

        counts_sorted = sorted(counts.items(), key=lambda x:-x[1])

        ret = {
            'counts' : counts_sorted,
            'keywords' : keywords
        }

        fw.write(self.__result_path, ret)

    def __extraKeyWord(self, datas):
        ret = []
        for data in datas:
            if 'title' in data:
                title_keywords = self.__cotoha.keyword(data['title'])
                if not title_keywords:
                    continue

                story_keywords = self.__cotoha.keyword(data['story'])
                if not story_keywords:
                    continue

                total_keywords = self.__removeDuplicate(title_keywords, story_keywords)

                result = {
                    'title' : data['title'],
                    'daily_point' : data['daily_point'],
                    'title_keywords' : title_keywords,
                    'story_keywords' : story_keywords,
                    'total_keywords' : total_keywords
                }
                ret.append(result)

        return ret

    def __removeDuplicate(self, *args):
        ret = []
        for arg in args:
            for data in arg:
                if data['form'] not in ret:
                    ret.append(data['form'])

        return ret

    def __countKeyWord(self, keywords):
        ret = {}
        for keyword in keywords:
            for word in keyword['total_keywords']:
                ret.setdefault(word, 0)
                ret[word] += 1

        return ret
