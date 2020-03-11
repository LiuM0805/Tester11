from test_selenium.page.manage import Manage


class TestManage:
    def setup(self):
        self.manage = Manage(reuse=True)

    def test_material(self):
        self.manage.material(
            "/Users/liumiao/PycharmProjects/Tester11/test_selenium/testcase/热火.jpg")
        assert "热火.jpg" in self.manage.upload_status()