import collections

T = int(input())
inputList = []

for _ in range(T):
    N = input()
    inputList.append(N)

for i, case in enumerate(inputList):
    searchCounter = collections.Counter(case)
    changeNum = case
    isPossible = False
    k = 1
    while len(str(int(changeNum)*k)) == len(case):
        k += 1
        changeCounter = collections.Counter(str(int(changeNum)*k))
        if changeCounter == searchCounter:
            isPossible = True
            break

    if isPossible:
        print(f"#{i + 1} possible")
    else:
        print(f"#{i + 1} impossible")




