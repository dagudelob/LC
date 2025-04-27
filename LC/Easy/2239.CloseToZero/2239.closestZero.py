class Solution(object):
    def findClosestNumber(self, nums):
        max = nums[0]
        min = nums[0]
        i=0 
        while i < len(nums):
            if nums[i] > 0:
                if nums[i] > max:
                    max = nums[i]
            else:
                if nums[i] < min:
                    min = nums[i]
            i+=1
        if abs(max) > abs(min):
            return min
        else:
            return max



# Test del código
#nums = [-4, -2, -1, -4, -5, -3, 2, 1, 2, 3, 4]
nums = [-100000,-100000]
print(Solution().findClosestNumber(nums))  

