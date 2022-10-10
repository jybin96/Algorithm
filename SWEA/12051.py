T = int(input())

for i in range(T):
    N, PD, PG = map(int, input().split())
    result = False

    if PD != 0 and PG == 0:
        result = False
    elif PD != 100 and PG == 100:
        result = False

    else:
        for num in range(1, N + 1):
            if (num * PD) % 100 == 0:
                result = True
                break

    if result:
        print(f"#{i + 1} Possible")
    else:
        print(f"#{i + 1} Broken")
