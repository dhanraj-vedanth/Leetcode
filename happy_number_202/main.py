class Solution:
    def isHappy(self, n: int) -> bool:
        if n is None:
            return False
        if n == 1:
            return True
        seen_list = []
        while(n != 1):
            if n in seen_list:
                return False
            else:
                seen_list.append(n)
            numbers = [int(each) for each in str(n)]
            squared_nums = map(self.squared, numbers)
            new_n = 0
            for each in squared_nums:
                new_n += each
            n = new_n
            if n == 1:
                return True

    def squared(self, number):
        return number * number



