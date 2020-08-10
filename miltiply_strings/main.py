class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        ref_dict = {'0':0,'1':1, '2':2, '3':3,'4':4,'5':5,'6':6,'7':7,"8":8,'9':9}
        def callerfn(string):
            final_no = 0
            m = 1
            for num,each in enumerate(reversed(string)):
                # print(num,each)
                if num == 0:
                    conv_num = ref_dict[each]
                    final_no = conv_num
                    m = m * 10
                else:
                    conv_num = ref_dict[each]
                    # print(conv_num)
                    final_no = conv_num * m + final_no
                    m = m * 10
                # print(final_no)
                # print(m)
                # input()
            return final_no
        val1 = callerfn(num1)
        val2 = callerfn(num2)
        # print(val1)
        # print(val2)
        final_val = val1 * val2
        
        return str(final_val)
        
s = Solution()
s.multiply('24','110')    
        
                    
                
                
        