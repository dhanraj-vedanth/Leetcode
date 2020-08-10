class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        main_str = s
        sub_str = ''
        last_ins = 0
        first_time = 0
        previous_largest_ss = ''
        print(s)
        for num, each in enumerate(main_str):
            print(each)
            # if each not in sub_str:
            if first_time == 0:
                print("INGA DA")
                sub_str += str(each)
                last_ins = num
                first_time = 1
            elif first_time == 1:
                print("ULLA DA")
                print(each, sub_str[-1])
                if each != sub_str[-1]:
                    if (num - 1) == last_ins:
                        sub_str += str(each)
                        last_ins = num
                else:
                    print("OTHA KUNDI INGAYA")
                    if len(sub_str) > len(previous_largest_ss):
                        previous_largest_ss = sub_str
                    sub_str = ''
                    sub_str += each
                    last_ins = num
            print("Previous",previous_largest_ss)
            print("current",sub_str)
            input()
            # print('Substring',str(sub_str))
        if len(sub_str) > len(previous_largest_ss):
            print(sub_str)
            return(len(sub_str))
        else:
            print(previous_largest_ss)
            return(len(previous_largest_ss))





s = Solution()
answer = s.lengthOfLongestSubstring("dvdf")
print(answer)