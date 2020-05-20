import json

from jsonpath import jsonpath


class BaseApi:
    @classmethod
    def format(cls, r):
        cls.r = r
        print(json.dumps(r.json(), indent=2, ensure_ascii=False))

    def jsonpath(self, path, r=None):
        if r is None:
            r = self.r.json()
        return jsonpath(r, path)
