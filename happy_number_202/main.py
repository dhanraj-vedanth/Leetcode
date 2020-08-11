class Solution:
    def isHappy(self, n: int) -> bool:
        """
        Method to check if the number is a happy number
        """
        if n is None:
            return False
        seen_list = []
        while(n != 1):
            if n in seen_list:
                return False
            else:
                seen_list.append(n)
            numbers = [int(each) for each in str(n)]
            squared_nums = map(self.squared, numbers)
            n = sum(squared_nums)
        return True

    def squared(self, number):
        """
        Helper function to return the square of a number
        """
        return number * number



