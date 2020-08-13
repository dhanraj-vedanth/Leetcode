from main import Solution


def test_rotate_pass():
    rotate_obj = Solution()
    res = rotate_obj.rotate([1, 2, 3, 4, 5, 6, 7], 3)
    assert (res == [5, 6, 7, 1, 2, 3, 4])
