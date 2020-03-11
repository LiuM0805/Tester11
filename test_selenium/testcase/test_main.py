from test_selenium.page.main import Main


class TestMain:
    def setup(self):
        self.main = Main(reuse=True)

    def test_message(self):
        self.main.goto_messagelist()

    def test_add_member(self):
        self.main.goto_add_member().main_add_member()
        # assert 'aaa' in self.main.import_user().get_message()

    def test_import_user(self):
        self.main.goto_import_user().import_users(
            "/Users/liumiao/PycharmProjects/Tester11/test_selenium/testcase/通讯录批量导入模板.xlsx")
        # assert "xxx" in self.main.get_message()

    def test_send_message(self):
        send_page = self.main.goto_message().send(app="十一", group="十一", content="content")
        assert "content" in "|".join(send_page.get_history())
        print("|".join(send_page.get_history()))
