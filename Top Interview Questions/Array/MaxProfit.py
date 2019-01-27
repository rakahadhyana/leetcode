class Solution:
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        sum = 0
        for i in range(len(prices) - 1):
            if(prices[i+1] > prices[i]):
                sum += prices[i+1] - prices[i]
        return sum
        

if __name__ == "__main__":
    solution = Solution()
    print(solution.maxProfit([7,1,5,3,6,4]))