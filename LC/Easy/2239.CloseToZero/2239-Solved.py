class Solution:
    def minimo(self, nums: list[int]) -> int:
        a = min(nums, key=lambda x: (abs(x), -x)) # Encuentra el valor más cercano a 0 y lo devuelve
        return a

# Test del código
nums = [-4, -2, -1, -4, -5, -3, 2, 1, 2, 3, 4]
print(Solution().minimo(nums))


