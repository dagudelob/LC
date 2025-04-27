class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        min = 10**4
        max = prices[0]
        profit = 0 

        for i in range(len(prices)):
            if min > prices [i]:
                min = prices[i]
                max = prices[i]

            if max < prices [i]:
                max = prices[i]
                
                if profit < max - min:
                    profit = max - min  

        return profit