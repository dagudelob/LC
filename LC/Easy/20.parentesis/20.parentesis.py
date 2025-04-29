class Solution(object):
    def isValid(self, s):
        # contador 1 de "{" 
        count1 = 0
        # contador 2 de "("   
        count2 = 0
        # contador 3 de "["
        count3 = 0
        
        # hash 
        last = []
        
        for i in s:
            if i == "{":
                count1 += 1
                last.append("{")
            elif i == "(":
                count2 += 1
                last.append("(")
            elif i == "[":
                count3 += 1
                last.append("[")
            elif i == "}":
                # Check if the stack is not empty AND the top element is the matching opener
                if last and last[-1] == "{":
                    count1 -= 1
                    last.pop()
                else:
                    # Mismatch or closing bracket with no opener
                    return False
            elif i == ")":
                if last and last[-1] == "(":
                    count2 -= 1
                    last.pop()
                else:
                    return False
            elif i == "]":
                if last and last[-1] == "[":
                    count3 -= 1
                    last.pop()
                else:
                    return False


        if count1 == 0 and count2 == 0 and count3 == 0:
            return True
        else:
            return False
        
# test cases

print(Solution().isValid("()"))
print(Solution().isValid("()[]{}"))
print(Solution().isValid("(]))")) 
print(Solution().isValid("([])"))