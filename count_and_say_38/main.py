class Solution:
    def countAndSay(self,n):
        def helper(val):
            print(val)
            seen_str = ''
            result = ''
            for each in str(val):
                # print(each)
                lent = len(seen_str)
                if seen_str == '':
                    # print("here")
                    seen_str += each
                elif each == seen_str[lent-1]:
                    # print("now here")
                    seen_str  += each
                else:
                    # print("down low")
                    temp_len = len(seen_str)
                    result += str(temp_len)
                    result += str(seen_str)[0]
                    seen_str = str(each)
            if seen_str != '':
                # print("End reached with val in seen_str")
                temp_len = len(seen_str)
                result += str(temp_len)
                result += str(seen_str)[0]
            return result

        # print(helper(n))

        start = 1
        for i in range(n-1):
            start = helper(start)
            # print("NEW START", start)
            # input()
        return start
