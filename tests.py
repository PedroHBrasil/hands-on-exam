import unittest
from fibonacci import fibonacci
from palindrome import is_palindrome
from prime import is_prime
from sort import sort_desc


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


class TestPrime(unittest.TestCase):

    def test_prime1(self):
        self.assertIsNone(is_prime(0), "Should be False")

    def test_prime2(self):
        self.assertTrue(is_prime(1), "Should be True")

    def test_prime2(self):
        self.assertTrue(is_prime(2), "Should be True")

    def test_prime3(self):
        self.assertTrue(is_prime(3), "Should be True")

    def test_prime4(self):
        self.assertFalse(is_prime(4), "Should be False")

    def test_prime5(self):
        self.assertTrue(is_prime(5), "Should be True")

    def test_prime6(self):
        self.assertFalse(is_prime(6), "Should be False")

    def test_prime7(self):
        self.assertTrue(is_prime(7), "Should be True")

    def test_prime8(self):
        self.assertFalse(is_prime(8), "Should be False")

    def test_prime9(self):
        self.assertFalse(is_prime(9), "Should be False")

    def test_prime10(self):
        self.assertFalse(is_prime(10), "Should be False")


class TestSort(unittest.TestCase):

    def test_sort1(self):
        self.assertEqual(sort_desc([]), [], "Should be []")

    def test_sort2(self):
        self.assertEqual(sort_desc([1]), [1], "Should be [1]")

    def test_sort3(self):
        self.assertEqual(sort_desc([1, 2, 3]), [3, 2, 1],
                         "Should be [3, 2, 1]")

    def test_sort4(self):
        self.assertEqual(sort_desc([-10, 10.5, 0]), [10.5, 0, -10],
                         "Should be [10.5, 0, -10]")


if __name__ == '__main__':
    unittest.main()
