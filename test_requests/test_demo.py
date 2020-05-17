import json
from pprint import pprint

import requests
from jsonpath import jsonpath
from requests import Session, Response

proxies = {
    'http': 'http://127.0.0.1:8888',
    'https': 'http://127.0.0.1:8888',  # 只是https的区别
}
url_get = "http://httpbin.testing-studio.com/get"


def test_requests():
    r = requests.get("https://home.testing-studio.com/categories.json")
    pprint(r)
    pprint(r.json())
    assert r.status_code == 200


def test_get():
    r = requests.get("http://httpbin.testing-studio.com/get",
                     params={
                         "a": 1,
                         "b": 2,
                         "c": "ccc"
                     })
    print(r.json())
    assert r.status_code == 200


def test_post():
    r = requests.post("http://httpbin.testing-studio.com/post",
                      params={
                          "a": 1,
                          "b": 2,
                          "c": "ccc"
                      },
                      data={
                          "a": 11,
                          "b": 22,
                          "c": "cccddd"
                      },
                      headers={"h": "header demo"},
                      proxies=proxies,
                      verify=False
                      )
    print(r.json())
    assert r.status_code == 200
    assert r.json()["headers"]["H"] == "header demo"


def test_upload():
    url = "http://127.0.0.1/post"
    r = requests.post(
        url,
        files={"file": open("__init__.py", "rb")},
        # proxies=proxies,
        verify=False
        # headers={"Content-Type": "application/plain"},
        # cookies={"name": "liumiao"}
    )
    print(r.json())
    assert r.status_code == 200


def test_session():
    s = Session()
    s.proxies = proxies
    s.get(url_get)


def test_get_hook():
    def modify_response(r: Response, *args, **kwargs):
        r.demo = "OK HOOK SUCCESS"
        return r

    r = requests.get("http://httpbin.testing-studio.com/get",
                     params={
                         "a": 1,
                         "b": 2,
                         "c": "ccc"
                     },
                     hooks={"response": [modify_response]}
                     )
    print(r.json())
    print(r.demo)
    assert r.status_code == 200


def test_jsonpath():
    r = requests.get("https://home.testing-studio.com/categories.json")
    # print(json.dumps(json.loads(r.text), indent=2, ensure_ascii=False))
    # assert r.json()["category_list"]["categories"][0]["id"] == 16
    # 根据jsonpath语法进行定位断言
    print(jsonpath(r.json(), '$..categories[?(@.name=="开源项目")]')[0]["description"])
    assert jsonpath(r.json(), '$..categories[?(@.name=="开源项目")]')[0]["description"] == "开源项目交流与维护"
