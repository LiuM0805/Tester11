from unit.div import div



class Test_div_num():
    def test_div_int(self):
        assert div(10, 5) == 2
        assert div(18, 9) == 2

    def test_div_float(self):
        assert div(10.6, 5.3) == 2
        assert div(6.66, 3.3) == 2.018

    def test_div_except(self):
        assert div("a", "b") == 5
        assert div(10, "a") == 10

    def test_div_lang(self):
        assert div(1000000000000, 500000000000) == 2
