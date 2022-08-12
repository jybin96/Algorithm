def divisor(a):
    divisorList = [i for i in range(1, a + 1) if a % i == 0.0]
    return divisorList


def getItem(divisorList, k):
    if len(divisorList) < k:
        return 0
    else:
        return divisorList[k - 1]


data = list(map(int, input().split()))
print(getItem(divisor(data[0]), data[1]))
