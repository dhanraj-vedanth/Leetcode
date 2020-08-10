class Solution:
    def helper(self, val, val1,singles,list_op):
        print("singles",singles)
        if val:
            singles += [val]
        if val1:
            list_op += [val1]
        print("Singles",singles)
    def caller(self, lent,s,singles,list_op):
        start = 0
        while(start != lent):
            if s[start-1] == "0":
                print(s[start])
                start += 1
                break
            print(start)
            if start == 0:
                print("first case")
                val = s[start]
                print(val,'')
                input()
                self.helper(val,'',singles,list_op)
            else:
                # print("Other cases")
                val = s[start]
                val1 = s[start-1:start+1]
                print(val,val1)
                print(singles,'singlesdaw')
                input()
                if 0 < int(val1) <= 26:
                    self.helper(val,val1,singles,list_op)
                else:
                    self.helper(val,'',singles,list_op)
            start += 1
    def numDecodings(self, s: str) -> int:
        final_count = 0
        singles = []
        list_op = []
        lent = len(s)
        self.caller(lent,s,singles,list_op)
        print("Done")
        print(singles,list_op)
        if '0' not in singles:
            final_count += 1
        list_len = len(list_op)
        final_count += list_len
        return final_count

s = Solution()
s.numDecodings('1011')