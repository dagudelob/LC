class Solution(object):
    def findClosestNumber(self, nums):
        b = map(lambda x: (abs(x)), nums) # convierte los números a su valor absoluto
        a = min(b)  # escoge el mínimo de los números absolutos
        
        # escoge la posición del número en la lista original
        if a in nums:
            return a
        else: 
            return (-a)



# Test del código
#nums = [-4, -2, -1, -4, -5, -3, 2, 1, 2, 3, 4]
nums = [-100000,-100000]
print(Solution().findClosestNumber(nums))  

