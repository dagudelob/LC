class Solution(object):
    def isSubsequence(self, s, t):
    
     
        if not s:
            return True
        if not t:
            return False
        i = 0
        j = 0
        while j < len(t):
            if s[i] == t[j]:
                i += 1
                if i == len(s):
                    return True
            j += 1
        return False
        
#test Codigo:
print(Solution().seq("abc", "ajblkoijoijc"))  # Output: True
print(Solution().seq("axc", "ahbgdc"))  # Output: False
print(Solution().seq("", "ahbgdc")) # Output: True
print(Solution().seq("abc", "")) # Output: False
print(Solution().seq("axc", "ahbgdc")) # Output: False