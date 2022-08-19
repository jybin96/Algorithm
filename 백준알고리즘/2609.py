def GCD(x, y):
    while y:
        x, y = y, x % y
    return x


def LCM(x, y):
    result = (x * y) / GCD(x, y)
    return result


num = list(map(int, input().split()))

print(GCD(num[0], num[1]))
print(int(LCM(num[0], num[1])))