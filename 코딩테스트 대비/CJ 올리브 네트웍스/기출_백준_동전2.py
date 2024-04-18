import sys

sys.stdin = open("input.txt",'r')

n, k = map(int, input().split())

coins = [ int(input()) for _ in range(n)]


def min_coins(n, k, coins):
    # dp[i]는 i원을 만드는 데 필요한 최소 동전 수
    dp = [float('inf')] * (k + 1)
    dp[0] = 0  # 0원을 만드는 데는 0개의 동전이 필요
    print(coins)
    # 모든 동전에 대해 반복
    for coin in coins:
        for i in range(coin, k + 1):
            if dp[i - coin] != float('inf'):
                dp[i] = min(dp[i], dp[i - coin] + 1)
                print(coin,i,"-->",dp)

    # k원을 만드는 데 필요한 최소 동전 수 반환
    return dp[k] if dp[k] != float('inf') else -1


print(min_coins(n, k, coins))

