class Solution:
    def validPalindrome(self, s: str) -> bool:
        def ispalin(val):
            print(val)
            if val == val[::-1]:
                return True 
            else:
                return False
        counter = 0
        start = 0
        end = len(s) - 1
        while(start <= end):
            if s[start] != s[end] and counter == 0:
                counter += 1
                return ispalin(s[:start] + s[start+1:]) or ispalin(s[:end] + s[end +1:])
            start += 1
            end -= 1
        return True 

s = Solution()
print(s.validPalindrome("abc"))