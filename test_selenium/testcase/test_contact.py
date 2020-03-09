from test_selenium.page.contact import Contact


# 测试通讯录
class TestContact:
    def test_add_mamber(self):
        contact = Contact()
        contact.add_member("abc")
