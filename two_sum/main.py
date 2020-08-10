class Solution:
    def twoSum(self, nums, target):
        mapper = {}
        for each in range(len(nums)):
            if  (target - nums[each]) in mapper:
                print(each)
                print(target,nums[each])
                print(mapper[target-nums[each]])
                return [mapper[target-nums[each]],each]
            else:
                mapper[nums[each]] = each
            print(mapper)
            input()
                
        
s = Solution()
print(s.twoSum([2,3,4,7,10], 9))
