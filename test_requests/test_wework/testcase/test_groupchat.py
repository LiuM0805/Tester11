from test_requests.test_wework.api.groupchat import GroupChat


class TestGroupChat:

    @classmethod
    def setup_class(cls):
        cls.groupchat = GroupChat()

    # 获取客户群列表接口
    def test_groupchat_get(self):
        r = self.groupchat.list(offset=0, limit=10)
        assert r["errcode"] == 0

    # 获取客户群列表，且新增接口入参
    def test_groupchat_get_status(self):
        r = self.groupchat.list(offset=0, limit=10, status_filter=0)
        assert r["errcode"] == 0

    # 获取客户群详情接口
    def test_groupchat_detail(self):
        # 获取客户群列表的chat_id
        r = self.groupchat.list(offset=0, limit=10)
        chat_id = r["group_chat_list"][0]["chat_id"]

        # 把列表的出参chat_id传递给详情接口做入参
        r = self.groupchat.get(chat_id=chat_id)
        assert r["errcode"] == 0
        assert len(r["group_chat"]["member_list"]) > 0
