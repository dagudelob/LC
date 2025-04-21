class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        for i in range(len(nums)): 
            for j in range(i + 1, len(nums)):
                if target == nums[i] + nums[j]:
                    return [i, j]
        return None

# Test del código
nums = [2,7,11,15]
target = 9

print(Solution().twoSum(nums, target))

