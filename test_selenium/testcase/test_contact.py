from test_selenium.page.contact import Contact


# 通讯录页
class TestContact:
    def setup(self):
        self.contact = Contact(reuse=True)

    # 添加用户
    def test_add_member(self):
        self.contact.add_member("aaa", "123", "18810143185")
        assert self.contact.assert_value() == "保存成功"

    # 编辑用户
    def test_edit_member(self):
        self.contact.edit_member2("测试", "11111111111")
        assert self.contact.assert_value() == "保存成功"

    # 删除用户
    def test_delete_member(self):
        self.contact.delete_member()
        assert self.contact.assert_value() == "正在删除..."
