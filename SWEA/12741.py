T = int(input())

cases = [list(map(int, input().split())) for _ in range(T)]

for i, case in enumerate(cases):
    a = case[0]
    b = case[1]
    c = case[2]
    d = case[3]
    result = 0
    start = max(a, c)
    end = min(b, d)
    if start < end:
        result = end - start

    print(f"{i + 1} {result}")