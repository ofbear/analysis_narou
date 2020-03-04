import json
import os

from lib.apinarou import ApiNarou
from lib.cotohakeyword import CotohaKeyword
from lib.cotohasimilarity import CotohaSimilarity
from lib.filewrapper import fw

class SystemSpecific():
    def __init__(self, reload=False):
        current_dir = os.getcwd()

        conf = fw.read(f'{current_dir}\\conf.json')
        if not conf:
            exit(1)
        self.__clientId = conf['cotoha']['clientId']
        self.__clientSecret = conf['cotoha']['clientSecret']

        self.__result_dir = f'{current_dir}\\result'
        if not os.path.isdir(self.__result_dir):
            os.makedirs(self.__result_dir, exist_ok=True)

        narou_path = f'{self.__result_dir}\\narou_data.txt'

        an = ApiNarou(obj=conf['narou'], reload=reload, path=narou_path)
        self.__novel_datas = an.data

    def keyword(self):
        ck = CotohaKeyword(
            self.__clientId,
            self.__clientSecret,
            self.__result_dir
        )
        ck.exec(self.__novel_datas)

    def similarity(self):
        cs = CotohaSimilarity(
            self.__clientId,
            self.__clientSecret,
            self.__result_dir
        )
        cs.exec(self.__novel_datas)
