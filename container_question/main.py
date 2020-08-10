class Solution:
    def maxArea(self, height):
        def compute(p1,p2,max_area):
            if p1 == p2:
                print(max_area)
                return 
            area = 0
            ar_cal = 0
            print(p1,p2,max_area)
            if height[p1]< height[p2]:
                ar_cal = height[p1]
                multiplier = p2 - p1
                area = multiplier * ar_cal
                if area > max_area:
                    max_ar = area
                compute(p1+1, p2, max_area)
            else:
                ar_cal = height[p2]
                multiplier = p2 - p1
                area = multiplier * ar_cal
                if area > max_area:
                    max_ar = area
                compute(p1,p2-1, max_area)
        max_ar = 0
        p2 = len(height)
         p2` -= 1
        p1 = 0
        if len(height) == 0 or len(height) == 1:
            return 0
        compute(p1,p2,0)
        print(max_area)
        return  

        
            
s = Solution()
s.maxArea([1,8,6,2,5,4,8,3,7])