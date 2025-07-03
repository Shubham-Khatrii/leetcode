class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        min_pri=prices[0]
        max_pro=0
        for i in prices:
            if min_pri>i:
                min_pri=i
            elif i-min_pri>max_pro:
                max_pro=i-min_pri
        return max_pro
        