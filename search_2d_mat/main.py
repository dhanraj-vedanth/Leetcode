class Solution:
    def searchMatrix(self, matrix, target) -> bool:
        
        self.match = 0
        for i in range(len(matrix)):
            self.binary_search(matrix[i],target)
            if self.match == 1:
                break
        
        return self.match == 1
    
    def binary_search(self,arr,target):
        print(arr)
        l = 0
        r = len(arr) - 1
        
        while l <= r:
            mid = (l + r)//2
            print(arr)
            print(l,r)
            print(mid)
            print(arr[mid])
            if arr[mid] == target:
                self.match = 1
                return
            if arr[mid] < target:
                print("in here",arr[mid],target)
                l = mid + 1
            else:
                r = mid - 1
            input()

s = Solution()

s.searchMatrix([[1,3,5,7],[10,11,16,20],[23,30,34,50]],13)
        
                