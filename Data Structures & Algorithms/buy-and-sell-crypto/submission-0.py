class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        lowest = sys.maxsize
        highest = 0
        Price_max = 0
        for i in range(len(prices)):
            diff =0 
            if lowest>prices[i]:
                lowest = min(lowest,prices[i])
            diff = prices[i]-lowest
            if Price_max < prices[i]-lowest:
                Price_max = diff
                highest = prices[i]
            #print(lowest, highest , diff, Price_max )
        return Price_max

