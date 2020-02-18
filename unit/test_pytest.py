import allure


def inc(x):
    return x + 1


def test_answer():
    assert inc(3) == 4
    allure.attach.file(r'/Users/liumiao/Desktop/图片/123.png', attachment_type=allure.attachment_type.PNG)


class TestClass:
    def test_one(self):
        x = "this"
        assert "h" in x

    def test_two(self):
        aa = TestClass()
        assert hasattr(aa , "test_two")
