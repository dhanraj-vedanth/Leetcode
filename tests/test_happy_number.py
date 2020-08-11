import unittest
from ..happy_number_202.main import Solution


class HappyTest(unittest.TestCase):
    def test_true(self):
        self.solution = Solution()
        self.assertEqual(self.solution.isHappy(19), True)
   
    def test_false(self):
        self.solution = Solution()
        self.assertEqual(self.solution.isHappy(5), False)
