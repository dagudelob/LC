class Solution(object):
    def longestCommonPrefix(self, strs): 
        # Initialize an empty list to store the characters of the common prefix.
        prefix = [] 
        
        # Handle the edge case where the input list is empty. 
        # If it's empty, there's no common prefix, so return an empty string.
        if not strs:
            return ""
            
        # Find the shortest string in the list.
        shortest_str = min(strs, key=len)
        print(f"min(strs, key=len): {min(strs, key=len)}")
        print(f"shortest_str: {shortest_str}")
        
        # Iterate through the characters of the shortest string.
        for i, char in enumerate(shortest_str):
            print(f"i: {i}, char: {char}")
            # Check if the character at the current position is the same in all strings.
            for other in strs:
                if other[i] != char:
                    # If a mismatch is found, return the prefix found so far.
                    return "".join(prefix)
            # If the character matches in all strings, add it to the prefix.
            prefix.append(char)

       

        # If all characters in the shortest string match, the shortest string is the common prefix.
        return "".join(prefix)

                            
                       
#Test Cases: 
# These lines create an instance of the Solution class and call the method.
# Due to the errors above, these calls will result in TypeErrors.
#print(Solution().longestCommonPrefix(["flower","flow","flight"]))
#print(Solution().longestCommonPrefix(["dog","racecar","car"]))
print(Solution().longestCommonPrefix(["doca","racecar","car"]))
