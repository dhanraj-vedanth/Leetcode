class Solution:
    def letterCasePermutation(self, S: str):
        def caller_fn(start,end,S,result):
            # print(start)
            if start == end:
                result.append(S)
                return
            if S[start].isalpha():
                temp1 = S[:start] + S[start].lower() + S[start+1:]
                temp2 = S[:start] + S[start].upper() + S[start+1:]
                # print(temp1,temp2)
                caller_fn(start+1,end,temp1,result)
                caller_fn(start+1,end,temp2,result)
                # print(start)
                # input()
            else:
                caller_fn(start+1,end,S,result)
    
        lent = len(S)
        start = 0
        end = lent -1
        result = []
        # print(start,end)
        caller_fn(start,end,S,result)
        print(result)

s = Solution()
s.letterCasePermutation('12345')