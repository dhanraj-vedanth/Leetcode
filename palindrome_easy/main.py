class Solution:
    def checker(self, val):
        if val.isalnum():
            return val
    def isPalindrome(self, s: str) -> bool:
        stripped = ""
        stripped += ''.join(list(filter(self.checker,s)))
        stripped = stripped.lower()
        if stripped == "":
            return True
        start = 0
        end = len(stripped) - 1

        while(start <= end):
            if stripped[start] == stripped[end]:
                start += 1
                end -= 1
            else:
                return False
        return True

s = Solution()
s.isPalindrome("A man, a plan, a canal: Panama")