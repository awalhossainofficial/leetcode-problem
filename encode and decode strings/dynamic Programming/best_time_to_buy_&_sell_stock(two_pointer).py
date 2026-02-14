
def maxProfit(prices):
    min_price = prices[0]
    max_profit = 0
    for price in prices:
        if  price < min_price:
            min_price = price
        else:
            profit = price - min_price

        max_profit = max(max_profit, profit)
    return max_profit

 

def maxProfit(self, prices: List[int]) -> int:
        l, r = 0,1
        maxP = 0

        while r < len(prices):
            if prices[l] < prices[r]:
                diff = prices[r] - prices[l]
                maxP = max(maxP, diff)
            else:
                l = r
            r +=1
        return maxP