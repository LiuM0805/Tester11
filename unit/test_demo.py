import unittest


class TestDemo(unittest.TestCase):
    def test_sum(self):
        x = 1 + 2
        print(x)
        self.assertEqual(4, x)

    def test_demo(self):
        self.assertTrue(False)


if __name__ == "__main__":
    unittest.main()
