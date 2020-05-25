import requests

from test_requests.test_wework.api.wework import WeWork


class Tag(WeWork):
    secret = "Sm8kkmUyqhD0AJqskJFJvcSLbs4RZQ_pkIvxC2b1LS4"  # 客户群的secret

    def __init__(self):
        self.data = self.api_load("../api/tag.api.yaml")

    def get_api(self):
        return self.api_send(self.data["get"])

    # def get(self):
    #     url = "https://qyapi.weixin.qq.com/cgi-bin/externalcontact/get_corp_tag_list"
    #     r = requests.post(
    #         url,
    #         params={"access_token": self.get_token(self.secret)},
    #         json={"tag_id": []}
    #     )
    #     self.format(r)
    #     return r.json()

    def add_api(self, name, **kwargs):
        self.params["name"] = name
        return self.api_send(self.data["add"])

    # def add(self, name, **kwargs):
    #     url = "https://qyapi.weixin.qq.com/cgi-bin/externalcontact/add_corp_tag"
    #     r = requests.post(
    #         url,
    #         params={"access_token": self.get_token(self.secret)},
    #         json={
    #             "group_id": "etBA9wCgAAQUL1mHqcgO7257bbZwjDew",
    #             "tag":
    #                 [
    #                     {
    #                         "name": name
    #                     }
    #                 ]
    #         }
    #     )
    #     self.format(r)
    #     return r.json()

    def update(self):
        pass

    def delete_api(self, tag_id=[], group_id=[]):
        self.params["tag_id"] = tag_id
        self.params["group_id"] = group_id
        return self.api_send(self.data["delete"])

    # def delete(self, tag_id=[], group_id=[]):
    #     url = "https://qyapi.weixin.qq.com/cgi-bin/externalcontact/del_corp_tag"
    #     r = requests.post(
    #         url,
    #         params={"access_token": self.get_token(self.secret)},
    #         json={
    #             "group_id": group_id,
    #             "tag_id": tag_id
    #         }
    #     )
    #     self.format(r)
    #     return r.json()
