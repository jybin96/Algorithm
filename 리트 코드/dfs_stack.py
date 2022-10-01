graph = {
    1: [2, 3, 4],
    2: [5],
    3: [5],
    4: [],
    5: [6, 7],
    6: [],
    7: [3]
}

discovered = []
stack = [1]
while stack:
    v = stack.pop()
    if v not in discovered:
        discovered.append(v)
        for w in graph[v]:
            stack.append(w)

print(discovered)
