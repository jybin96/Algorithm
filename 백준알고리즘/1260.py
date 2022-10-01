n = int(input())
m = int(input())
start = int(input())

dic = {}
for _ in range(m):
    temp = list(map(int, input().split()))
    if temp[0] not in dic:
        dic[temp[0]] = [temp[1]]
    elif temp[1] not in dic:
        dic[temp[1]] = []
    else:
        dic[temp[0]].append(temp[1])


def dfs(start) -> list:
    stack = [start]
    visit = []
    while stack:
        v = stack.pop(0)
        if v not in visit:
            visit.append(v)
            for w in dic[v]:
                stack.append(w)
    return visit

print(dic)
print(dfs(start))
