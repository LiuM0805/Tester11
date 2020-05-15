import requests

from test_requests.test_wework.api.baseapi import BaseApi
from test_requests.test_wework.api.wework import WeWork


class GroupChat(WeWork):
    secret = "Sm8kkmUyqhD0AJqskJFJvcSLbs4RZQ_pkIvxC2b1LS4"  # 客户群的secret

    # 客户群列表接口请求
    def list(self, offset, limit, **kwargs):
        data = {"offset": offset, "limit": limit}
        data.update(**kwargs)
        url = "https://qyapi.weixin.qq.com/cgi-bin/externalcontact/groupchat/list"
        r = requests.post(
            url,
            params={"access_token": self.get_token(self.secret)},
            json=data
        )
        BaseApi.format(r=r)
        return r.json()

    # 客户群详情接口请求
    def get(self, chat_id):
        detail_url = "https://qyapi.weixin.qq.com/cgi-bin/externalcontact/groupchat/get"
        r = requests.post(
            detail_url,
            params={"access_token": self.get_token(self.secret)},
            json={"chat_id": chat_id}
        )
        BaseApi.format(r=r)
        return r.json()
