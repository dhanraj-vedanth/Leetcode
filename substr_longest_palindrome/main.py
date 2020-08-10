class Solution:
    def longestPalindrome(self, s: str) -> str:
        # print(len(s))
        max_palin = ''
        for i in range(len(s)):
            for j in range(len(s)):
                print(i,j)
                print(s[i:j+1]) 
        #         print(s[i:j])
        #         print(s[i:j][::-1])
        #         if s[i:j] == s[i:j][::-1]:
        #             # print(len(s[i:j]))
        #             # print(len(s[i:j]),len(max_palin))
        #             if len(max_palin) <= len(s[i:j]):
        #                 print("in here")
        #                 max_palin = s[i:j]
        #         print(max_palin)
        #         input()
        # return max_palin
    
    
s = Solution()

ans = s.longestPalindrome('bb')
print(ans)