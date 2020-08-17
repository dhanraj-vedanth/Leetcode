from valid_palindrome_125.main import Solution


def test_positive_case():
    s = Solution()
    assert s.isPalindrome("A man, a plan, a canal: Panama") is True
