nums = list(map(int, input().split()))
nums.sort()
pair = []
sum = 0

for n in nums:
    pair.append(n)
    if len(pair) == 2:
        sum += min(pair)
        pair = []

print(sum)
