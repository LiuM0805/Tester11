from test_selenium.page.main import Main


class TestContact:
    def setup(self):
        self.main = Main(reuse=True)

    def test_add_mamber(self):
        self.main.goto_add_member().add_member()
        assert "测试" in self.main.goto_add_member().get_member()
