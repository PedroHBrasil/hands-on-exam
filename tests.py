import unittest
from fibonacci import fibonacci


class TestSum(unittest.TestCase):

    def test_fibonacci(self):
        self.assertEqual(fibonacci(0), 0, "Should be 0")

    def test_fibonacci(self):
        self.assertEqual(fibonacci(1), 1, "Should be 1")

    def test_fibonacci(self):
        self.assertEqual(fibonacci(2), 1, "Should be 1")

    def test_fibonacci(self):
        self.assertEqual(fibonacci(3), 2, "Should be 2")

    def test_fibonacci(self):
        self.assertEqual(fibonacci(4), 3, "Should be 3")

    def test_fibonacci(self):
        self.assertEqual(fibonacci(5), 5, "Should be 5")

    def test_fibonacci(self):
        self.assertEqual(fibonacci(6), 8, "Should be 8")

    def test_fibonacci(self):
        self.assertEqual(fibonacci(7), 13, "Should be 13")

    def test_fibonacci(self):
        self.assertEqual(fibonacci(8), 21, "Should be 21")


if __name__ == '__main__':
    unittest.main()
