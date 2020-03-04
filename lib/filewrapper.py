import json
import os

class fw():
    @staticmethod
    def write(path, data):
        if os.path.isfile(path):
            os.remove(path)

        with open(path, 'w', encoding="utf-8") as f:
            json.dump(data, f, indent=4, ensure_ascii=False)

    @staticmethod
    def read(path):
        if not os.path.isfile(path):
            return False

        with open(path, "r", encoding="utf-8") as f:
            return json.load(f)
