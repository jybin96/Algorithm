import sys

prices = list(map(int, input().split()))
min_price = sys.maxsize
profit = 0

# 최솟값과 최대값을 계속 갱신
for price in prices:
    min_price = min(min_price, price)
    profit = max(profit, price - min_price)

print(profit)