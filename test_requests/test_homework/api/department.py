import requests

from test_requests.test_homework.api.baseapi import BaseApi


class Department(BaseApi):
    _contacts_secret = "K5JdBESxxB-hM1woDSR-8HB5DBQnN936uOoTp4lNtKo"  # 通讯录同步的secret
    _token_url = "https://qyapi.weixin.qq.com/cgi-bin/gettoken"  # token请求地址
    _corpid = "wwe6da3b113fc1b2ab"  # 必填参数：企业corpid
    _token = dict()  # 以词典形式存放secret和token的值

    # 用于测试token是否获取成功，所以它返回所有响应json内容
    def get_access_token(self):
        r = requests.get(
            self._token_url,
            params={"corpid": self._corpid, "corpsecret": self._contacts_secret}
        )
        self._json_format(jq=r)
        return r.json()

    # 用于给其他接口做token入参使用，所以它返回的只有token值
    def get_token(self, secret=_contacts_secret):
        # 防止重复访问，判断已有的secret是否存在这个词典里
        if secret not in self._token.keys():
            # 没有的话，重新请求token接口
            r = requests.get(
                self._token_url,
                params={"corpid": self._corpid, "corpsecret": self._contacts_secret}
            )
            # 将请求的token单独拿出来给词典的secret这个key值里，保存形式secret[key] = token
            self._token[secret] = r.json()["access_token"]
        # 返回secret就等于返回key的值，就是token
        return self._token[secret]

    # 获取部门列表
    def select_depart(self):
        select_url = "https://qyapi.weixin.qq.com/cgi-bin/department/list"
        r = requests.get(
            select_url,
            params={"access_token": self.get_token()}
        )
        self._json_format(jq=r)
        return r.json()

    # 创建部门
    def create_depart(self, name, departid=1):
        create_url = "https://qyapi.weixin.qq.com/cgi-bin/department/create"
        r = requests.post(
            create_url,
            params={"access_token": self.get_token()},
            json={"name": name, "parentid": departid}
        )
        self._json_format(jq=r)
        return r.json()

    # 更能部门
    def update_depart(self, id, **kwargs):
        data = {"id": id}
        data.update(**kwargs)
        update_url = "https://qyapi.weixin.qq.com/cgi-bin/department/update"
        r = requests.post(
            update_url,
            params={"access_token": self.get_token()},
            json=data
        )
        self._json_format(jq=r)
        return r.json()

    # 删除部门
    def delete_depart(self, id):
        delete_url = "https://qyapi.weixin.qq.com/cgi-bin/department/delete"
        r = requests.get(
            delete_url,
            params={"access_token": self.get_token(), "id": id}
        )
        self._json_format(jq=r)
        return r.json()
