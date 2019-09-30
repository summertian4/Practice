class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        dValues = []
        result = 0
        for i in range(1, len(prices)):
            dValues.append(prices[i] - prices[i - 1])
        for i in dValues:
            if i > 0:
                result += i
        return result