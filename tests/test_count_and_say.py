from count_and_say_38.count_and_say import Solution


def test_count_success():
    s = Solution()
    assert (s.countAndSay(5) == "111221")
