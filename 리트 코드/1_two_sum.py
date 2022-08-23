nums = list(map(int, input().split()))
target = int(input())

for i, n in enumerate(nums):
    complement = target - n
    if complement in nums[i+1:]:
        print([nums.index(n), nums[i+1:].index(complement)+(i+1)])

