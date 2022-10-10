import math

T = int(input())

for i in range(T):
    case = list(map(int, input().split()))
    N = case[0]
    D = case[1]
    between = 2 * D + 1
    print(f"#{i + 1} {math.ceil(N / between)}")
