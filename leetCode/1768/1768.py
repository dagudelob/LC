class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        sol = []
        for i in range(max(len(word1), len(word2))):
            if i < len(word1):
                sol.append(word1[i])
            if i < len(word2):
                sol.append(word2[i])
        return ''.join(sol)  # Convierte la lista en una cadena
    
# Testing the function
solution = Solution()
print(solution.mergeAlternately("abc", "abcd"))