import unittest


class TestDemo(unittest.TestCase):
    def test_sum(self):
        x = 1 + 2
        print(x)
        self.assertEqual(3, x)

    def test_demo(self):
        self.assertTrue(1+1)


if __name__ == "__main__":
    unittest.main()
