import collections

T = int(input())

for i in range(T):
    S = input()
    result = True
    counter = collections.Counter(S)

    for key, value in counter.items():
        if value != 2:
            result = False
            break

    if result:
        print(f"#{i + 1} Yes")
    else:
        print(f"#{i + 1} No")
