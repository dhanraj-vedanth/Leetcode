class Solution:
    def countAndSay(self, n: int) -> str:
        if n == 1:
            return "1"
        final_string = "1"
        for _ in range(1, n):
            previous = final_string[0]
            count = 0
            temp_string = ""
            for each_string in final_string:
                if each_string is not previous:
                    temp_string += str(count) + previous
                    previous = each_string
                    count = 1
                else:
                    count += 1
            temp_string += str(count) + previous
            final_string = temp_string
        return final_string

