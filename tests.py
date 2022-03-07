import unittest
from fibonacci import fibonacci
from palindrome import is_palindrome


class TestFibonacci(unittest.TestCase):

    def test_fibonacci0(self):
        self.assertEqual(fibonacci(0), 0, "Should be 0")

    def test_fibonacci1(self):
        self.assertEqual(fibonacci(1), 1, "Should be 1")

    def test_fibonacci2(self):
        self.assertEqual(fibonacci(2), 1, "Should be 1")

    def test_fibonacci3(self):
        self.assertEqual(fibonacci(3), 2, "Should be 2")

    def test_fibonacci4(self):
        self.assertEqual(fibonacci(4), 3, "Should be 3")

    def test_fibonacci5(self):
        self.assertEqual(fibonacci(5), 5, "Should be 5")

    def test_fibonacci6(self):
        self.assertEqual(fibonacci(6), 8, "Should be 8")

    def test_fibonacci7(self):
        self.assertEqual(fibonacci(7), 13, "Should be 13")

    def test_fibonacci8(self):
        self.assertEqual(fibonacci(8), 21, "Should be 21")


class TestPalindrome(unittest.TestCase):

    def test_palindrome1(self):
        self.assertTrue(is_palindrome(""), "Should be True")

    def test_palindrome2(self):
        self.assertTrue(is_palindrome("ana"), "Should be True")

    def test_palindrome3(self):
        self.assertTrue(is_palindrome("anna"), "Should be True")

    def test_palindrome4(self):
        self.assertFalse(is_palindrome("pedro"), "Should be False")

    def test_palindrome5(self):
        self.assertFalse(is_palindrome("apedroa"), "Should be False")


if __name__ == '__main__':
    unittest.main()
