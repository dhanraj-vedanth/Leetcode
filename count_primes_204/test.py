import unittest
from count_primes_204.main import Solution


class PrimeTest(unittest.TestCase):
    def test_success(self):
        solution = Solution()
        result = solution.countPrimes(10)
        self.assertEqual(result, 4)
