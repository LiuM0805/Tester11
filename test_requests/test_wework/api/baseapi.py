import json


class BaseApi:
    @classmethod
    def format(self, r):
        print(json.dumps(r.json(), indent=2))
