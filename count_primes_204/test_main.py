# import unittest
# from count_primes_204.main import Solution
from main import Solution


def test_count_primt():
    solution = Solution()
    result = solution.countPrimes(10)
    assert result == 4


# class PrimeTest(unittest.TestCase):
#     def test_success(self):
#         solution = Solution()
#         result = solution.countPrimes(10)
#         self.assertEqual(result, 4)