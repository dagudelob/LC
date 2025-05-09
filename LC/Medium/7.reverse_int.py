class Solution:
    def reverse(self, x: int) -> int:
         
        neg = int(x) < 0
        x = abs(x)
        rx = 0 
        while x > 0:
            rx = x%10  + rx *10
            x = x//10

        if neg:
            rx = -rx

        if rx > 2**31-1 or rx < -2**31:    
            return 0
        
        return rx 


x = -123
print(Solution().reverse(x))

# Output: -321