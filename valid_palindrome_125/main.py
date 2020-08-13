class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = s.replace(" ", "")
        new_s = ""
        for each in s:
            if each.isalnum():
                new_s += each
        new_s = new_s.lower()
        if new_s == new_s[::-1]:
            return True
        else:
            return False
