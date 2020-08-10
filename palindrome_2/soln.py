class Solution:
    def validPalindrome(self, s: str) -> bool:
        l, r = 0, len(s)-1
        def isPalin(s):
            print(s)
            print(s[::-1])
            return s==s[::-1] 
        while l<r:
            if s[l]!=s[r]:
                print(s[l+1:r+1], s[l:r])
                return isPalin(s[l+1:r+1]) or isPalin(s[l:r])
            l += 1
            r -= 1
        return True

s = Solution()
print(s.validPalindrome("cbcc"))