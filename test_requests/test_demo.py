from pprint import pprint

import requests


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
                     data={
                         "a": 1,
                         "b": 2,
                         "c": "ccc"
                     })
    print(r.json())
    assert r.status_code == 200
