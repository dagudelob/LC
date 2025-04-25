class Solution(object):
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        deci=0
        if s.count("M") > 4 or s.count("D") > 1 or s.count("C") > 4 or s.count("L") > 1 or s.count("X") > 4 or s.count("V") > 1 or s.count("I") > 3:
            #print("Error: el número romano no es válido")
            raise ValueError("Error: el número romano no es válido")
        
        i = len(s) - 1
        while i >= 0:
            if s[i] == "I":
                deci += 1
            elif s[i] == "V":
                if i > 0 and s[i-1] == "I":
                    deci += 4
                    i -= 1
                else:
                    deci += 5
            elif s[i] == "X":
                if i > 0 and s[i-1] == "I":
                    deci += 9
                    i -= 1
                else:
                    deci += 10
            elif s[i] == "L":
                if i > 0 and s[i-1] == "X":
                    deci += 40
                    i -= 1
                else:
                    deci += 50
            elif s[i] == "C":
                if i > 0 and s[i-1] == "X":
                    deci += 90
                    i -= 1
                else:
                    deci += 100
            elif s[i] == "D":
                if i > 0 and s[i-1] == "C":
                    deci += 400
                    i -= 1
                else:
                    deci += 500
            elif s[i] == "M":
                if i > 0 and s[i-1] == "C":
                    deci += 900
                    i -= 1
                else:
                    deci += 1000
            else:
               #print("Error: el caracter no es un número romano")
                raise ValueError("Error: el caracter no es un número romano")
            i -= 1  
        return deci

#test use 

print(Solution().romanToInt("XII"))