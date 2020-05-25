import json

import requests
import yaml
from jsonpath import jsonpath


class BaseApi:
    params = {}

    @classmethod
    def format(cls, r):
        cls.r = r
        print(json.dumps(r.json(), indent=2, ensure_ascii=False))

    def jsonpath(self, path, r=None):
        if r is None:
            r = self.r.json()
        return jsonpath(r, path)

    @classmethod
    def yaml_load(cls, path) -> list:
        with open(path) as f:
            return yaml.safe_load(f)

    def api_load(self, path):
        return self.yaml_load(path)

    def api_send(self, req: dict):
        req["params"]["access_token"] = self.get_token(self.secret)
        raw = yaml.dump(req)
        for key, value in self.params.items():
            raw = raw.replace(f"${{{key}}}", repr(value))
        req = yaml.safe_load(raw)

        r = requests.request(
            method=req["method"],
            url=req["url"],
            params=req["params"],
            json=req["json"]
        )
        self.format(r)
        return r.json()
