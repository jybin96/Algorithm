nums = list(map(int, input().split()))
out = []
p = 1
# 왼쪽 곱셈
for i in range(len(nums)):
    out.append(p)
    p = p * nums[i]

p = 1
#왼쪽에서 오른쪽 값을 차례대로 곱셈
for i in range(len(nums)-1, 0 - 1, -1):
    out[i] = out[i] * p
    p = p * nums[i]

print(out)
