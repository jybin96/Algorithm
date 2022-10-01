import collections
import heapq

nums = list(map(int, input().split()))
k = int(input())
counter = collections.Counter(nums)
heap = []
result = []
for c in counter:
    heapq.heappush(heap, (-counter[c], c))

for _ in range(k):
    result.append(heapq.heappop(heap)[1])

print(result)