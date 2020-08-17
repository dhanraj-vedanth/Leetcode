from merge_sorted_array_88.main import Solution


def test_positive():
    s = Solution()
    assert (s.merge(
        [1, 2, 3, 0, 0, 0],
        3,
        [2, 5, 6],
        3
    ) == [1, 2, 2, 3, 5, 6])