import collections
from collections import deque

T = int(input())

S_list = deque(input() for _ in range(T))

for i in range(T):
    S = S_list.popleft()
    count = collections.Counter(S)
    remain_match = 15 - len(S)
    win = count.get("o")
    if win is None:
        win = 0

    if win + remain_match >= 8:
        print(f"#{i + 1} YES")
    else:
        print(f"#{i + 1} NO")