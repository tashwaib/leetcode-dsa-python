def best_time_to_buy_and_sell_stocks_2(prices):
    maxprofit=0
    for i in range(1,len(prices)):
        if prices[i]>prices[i-1]:
            maxprofit=maxprofit+prices[i]-prices[i-1]
    return maxprofit        
print(best_time_to_buy_and_sell_stocks_2([7,1,5,3,6,4]))

