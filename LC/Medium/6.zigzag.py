class Solution:
    def convert(self, s: str, numRows: int):
        

        if numRows == 1 or numRows >= len(s):
            return s
        rows = [''] * numRows
        cur_row = 0
        going_down = False
        for c in s:
            rows[cur_row] += c
            if cur_row == 0:
                going_down = True
            elif cur_row == numRows - 1:
                going_down = False
            if going_down:
                cur_row += 1
            else:
                cur_row -= 1
        return ''.join(rows)

print(Solution().convert("PAYPALISHIRING", 2))
# Output: "PAHNAPLSIIGYIR"

    