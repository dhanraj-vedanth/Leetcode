class Solution:
    def __init__(self):
        self.mapping = {
            '2': ['a', 'b', 'c'],
            '3': ['d', 'e', 'f'],
            '4': ['g','h','i'],
            '5': ['j','k','l'],
            '6': ['m','n','o'],
            '7': ['p','q','r','s'],
            '8': ['t','u','v'],
            '9': ['w','x','y','z']
        }
        
        
    def letterCombinations(self, digits: str, s):
        print("hello",digits,s)
        input()
        if len(digits) == 0:
            print("inga da")
            print('bello',s)
            input()
            if s == '':
                return []
            else:
                return [s]
        result = []
        print("result da")
        print(result)
        new_digit = digits[1:]
        for each in self.mapping[digits[0]]:
            result += self.letterCombinations(new_digit,s+each)
        return result

s = Solution()

result = s.letterCombinations("23",'')
print(result)