class Solution(object):
    def isPalindrome(self, x): 
        y = x
        inv = 0
        while y > 0  :
            inv = y%10 + inv*10 
            y = y//10
            
            '''print (f"inv: {inv}")
            print (f"x//10: {x//10}")
            print (f"y = {y}") '''           

        print(f"inv: {inv}")
        print(f"x: {x}")
        return inv == x 
print(f'Es Palindromo ? {Solution().isPalindrome(12321)}')
print(f'Es Palindromo ? Solution().isPalindrome(123321)')
print(Solution().isPalindrome(123321))
print(Solution().isPalindrome(121))