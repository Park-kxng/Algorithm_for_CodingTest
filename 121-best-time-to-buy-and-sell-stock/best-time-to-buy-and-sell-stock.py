class Solution(object):
    def maxProfit(self, prices):
        if not prices or len(prices) < 2:
            return 0

        min_price = prices[0]
        max_profit = 0

        for price in prices[1:]:
            if price < min_price:
                min_price = price
            else:
                max_profit = max(max_profit, price - min_price)

        return max_profit


        # # 무조건 작은 인덱스에서 큰 인덱스를 빼서 이익을 구해야함 - 주식의 이익
        # # 반복문을 돌면서 현재 날짜보다 뒤에서 팔았을 때 가장 높은 이익을 저장
        # answer = 0
        # for i in prices:
        #     if prices.index(i) != len(prices)-1:
        #         days = prices[prices.index(i)+1 :]
        #         output = max(days) - i
        #         if output > answer:
        #             answer = max(output)
        #     else:
        #         continue
        # if not prices or len(prices) < 2:
        #     return 0
    
        # max_profit = 0
        # min_price = prices[0]
        
        # for price in prices[1:]:
        #     max_profit = max(max_profit, price - min_price)
        #     min_price = min(min_price, price)
    
        #return profit
    
         