class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        #  [3,3,5,0,0,3,1,4]
        # (3-0) + (4-1) = (4-(1-(3-0)) = 6 
        # (buy1-sell1) + (buy2-sell2) = (sell1-(buy1-(buy2-sell2)))
        # for cases when buy1-sell1 is the max, still works 1,2,3,4 (4-(4-(4-1)))
        
        buy1 = float('inf')
        AdjustedBuy2 = float('inf')
        singleMaxProfit = 0
        maxProfit = 0
        #loop prices, whether is most gets kepted even k=2 get discard
        #whether min is send to sells, max get send to buys
        for price in prices:
            # lowest price encountered
            buy1 = min(buy1, price)
            # single max profit
            singleMaxProfit = max(singleMaxProfit, price-buy1)
            # 2nd price after adjustment with singleMaxProfit
            AdjustedBuy2= min(AdjustedBuy2, price-singleMaxProfit)
            # max so far
            maxProfit = max(maxProfit, price - AdjustedBuy2)
        return maxProfit
    
        # if profit1 is 