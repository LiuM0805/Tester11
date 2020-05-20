from test_requests.test_wework.api.tag import Tag


class TestTag:
    @classmethod
    def setup_class(cls):
        cls.tag = Tag()

    def test_get(self):
        r = self.tag.get()
        assert r["errcode"] == 0
        # print(self.tag.jsonpath("$..tag[?(@.name!='')]"))
        # print(self.tag.jsonpath("$..tag"))
        # print(self.tag.jsonpath("$..tag[?(@.name=='核心')]")[0]['id'])

    def test_add(self):
        r = self.tag.add("demo2")
        assert r["errcode"] == 0

    def test_delete(self):
        name = "demo2"

        # 如果demo2存在，就删除
        self.tag.get()
        x = self.tag.jsonpath(f"$..tag[?(@.name=='{name}')]")
        print(x)
        if isinstance(x, list) and len(x) > 0:
            self.tag.delete(tag_id=[x[0]['id']])

        # 如果干净后，开始测试
        self.tag.get()
        path = "$..tag[?(@.name!='')]"
        size = len(self.tag.jsonpath(path))

        # 添加新标签
        self.tag.add(name)
        self.tag.get()
        assert len(self.tag.jsonpath(path)) == size + 1

        # 删除新标签
        self.tag.get()
        tag_id = self.tag.jsonpath(f"$..tag[?(@.name=='{name}')]")[0]["id"]
        self.tag.delete(tag_id=[tag_id])

        # 断言
        self.tag.get()
        assert len(self.tag.jsonpath(path)) == size
