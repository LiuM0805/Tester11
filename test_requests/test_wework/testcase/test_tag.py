import pytest

from test_requests.test_wework.api.baseapi import BaseApi
from test_requests.test_wework.api.tag import Tag


class TestTag:
    # 读取yaml文件
    data = BaseApi.yaml_load("test_tag.data.yaml")
    steps = BaseApi.yaml_load("test_tag.step.yaml")

    @classmethod
    def setup_class(cls):
        cls.tag = Tag()

    def test_get_api(self):
        r = self.tag.get_api()
        assert r["errcode"] == 0

    # def test_get(self):
    #     r = self.tag.get()
    #     assert r["errcode"] == 0
    #     print(self.tag.jsonpath("$..tag[?(@.name!='')]"))
    #     print(self.tag.jsonpath("$..tag"))

    def test_add_api(self):
        r = self.tag.add_api("demo2")
        assert r["errcode"] == 0

    # def test_add(self):
    #     r = self.tag.add("demo2")
    #     assert r["errcode"] == 0

    @pytest.mark.parametrize("name", [
        "demo1"
    ])
    def test_delete_step(self, name):
        self.tag.params = {"name": name}
        self.tag.steps_run(self.steps["test_delete"])

    @pytest.mark.parametrize("name", data["test_delete"])
    def test_delete_api(self, name):
        # 如果name存在，就删除
        self.tag.get_api()
        x = self.tag.jsonpath(f"$..tag[?(@.name=='{name}')]")
        print(x)
        if isinstance(x, list) and len(x) > 0:
            self.tag.delete_api(tag_id=[x[0]['id']])

        # 如果干净后，开始测试
        self.tag.get_api()
        path = "$..tag[?(@.name!='')]"
        size = len(self.tag.jsonpath(path))

        # 添加新标签
        self.tag.add_api(name)
        self.tag.get_api()
        assert len(self.tag.jsonpath(path)) == size + 1

        # 删除新标签
        self.tag.get_api()
        tag_id = self.tag.jsonpath(f"$..tag[?(@.name=='{name}')]")[0]["id"]
        self.tag.delete_api(tag_id=[tag_id])

        # 断言
        self.tag.get_api()
        assert len(self.tag.jsonpath(path)) == size

    # 参数化
    # @pytest.mark.parametrize("name", [
    #     "demo1", "demo2", "中文", "😈_嘿嘿", " "
    # ])
    # 测试数据的数据驱动，读取文件
    # @pytest.mark.parametrize("name", data["test_delete"])
    # def test_delete(self, name):
    #     # 如果name存在，就删除
    #     self.tag.get()
    #     x = self.tag.jsonpath(f"$..tag[?(@.name=='{name}')]")
    #     print(x)
    #     if isinstance(x, list) and len(x) > 0:
    #         self.tag.delete(tag_id=[x[0]['id']])
    #
    #     # 如果干净后，开始测试
    #     self.tag.get()
    #     path = "$..tag[?(@.name!='')]"
    #     size = len(self.tag.jsonpath(path))
    #
    #     # 添加新标签
    #     self.tag.add(name)
    #     self.tag.get()
    #     assert len(self.tag.jsonpath(path)) == size + 1
    #
    #     # 删除新标签
    #     self.tag.get()
    #     tag_id = self.tag.jsonpath(f"$..tag[?(@.name=='{name}')]")[0]["id"]
    #     self.tag.delete(tag_id=[tag_id])
    #
    #     # 断言
    #     self.tag.get()
    #     assert len(self.tag.jsonpath(path)) == size
