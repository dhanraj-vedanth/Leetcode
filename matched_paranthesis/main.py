class Solution:
    def generateParenthesis(self, n):
        def gen_paranthesis(left,right,temp_str):
            # print(left,right,temp_str)
            if left == 0 and right == 0:
                print("Base case")
                print(left,right,temp_str)
                input()
                output_list.append(temp_str)
                return 
            else:
                if left >= right:
                    print("first")                    
                    print(left-1,right,temp_str,'(')
                    input()
                    gen_paranthesis(left-1,right,temp_str+'(')
                    
                elif left < right:
                    if left > 0:
                        gen_paranthesis(left-1,right,temp_str+'(')
                    print("Second")
                    print(left-1,right,temp_str,'(')
                    input()
                    gen_paranthesis(left,right-1,temp_str+')')
        output_list = []
        left = n
        right = n
        #dict_ = {'l':'(','r':'('}
        gen_paranthesis(left,right,'')
        
        print(output_list)


s = Solution()
s.generateParenthesis(3)
                    
                    
                    
                    
            
        