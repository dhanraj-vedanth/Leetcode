import unittest
from reverse_ll_206.main import generatelist, Solution


class ReverseTest(unittest.TestCase):
    def setUp(self):
        self.generated_head = generatelist([1, 2, 3, 4, 5])

    def test_reverse_success(self):
        solution = Solution()
        reversed_head = solution.reverseList(self.generated_head)
        reversed_list = []
        while reversed_head is not None:
            reversed_list.append(reversed_head.val)
            reversed_head = reversed_head.next
        self.assertEqual(reversed_list, [5, 4, 3, 2, 1])
