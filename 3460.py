def findBinaryBit(testCase):
    for _ in range(testCase):
        n = str(bin(int(input()))[2:][::-1])
        for i in range(0, len(n)):
            if str(1) == n[i]:
                print(i, end=' ')


T = int(input())
findBinaryBit(T)

