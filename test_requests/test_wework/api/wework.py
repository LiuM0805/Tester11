import json

import requests

from test_requests.test_wework.api.baseapi import BaseApi


class WeWork(BaseApi):
    corpid = "wwe6da3b113fc1b2ab"
    secret = "kdNMmelWqTOO8tjYyJDcB2F1zCx_U6qIlMeVhjGi-A0"  # python11期的应用
    token_url = "https://qyapi.weixin.qq.com/cgi-bin/gettoken"
    token = dict()

    @classmethod
    def get_access_token(cls):
        r = requests.get(
            cls.token_url,
            params={"corpid": cls.corpid, "corpsecret": cls.secret}
        )
        print(json.dumps(r.json(), indent=2))
        return r.json()

    @classmethod
    def get_token(cls, secret=secret):
        # 避免重复请求，提高速度
        if secret not in cls.token.keys():
            r = cls.get_access_token()
            # secret以key存放在token里，{secret:token值}
            cls.token[secret] = r["access_token"]
        return cls.token[secret]
