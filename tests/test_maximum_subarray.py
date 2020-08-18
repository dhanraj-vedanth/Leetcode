from maximum_subarray_53.main import Solution


def test_positive():
    s = Solution()
    assert (s.maxSubArray([-2, 1, -3, 4, -1, 2, 1, -5, 4]) == 6)
