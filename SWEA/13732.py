from collections import deque


def view(square, graph):
    len_sq = len(square) ** (0.5)
    if len_sq % 1 != 0:
        return "no"

    x, y = square.popleft()
    for i in range(x, x + int(len_sq)):
        for j in range(y, y + int(len_sq)):
            if graph[i][j] != "#":
                return "no"

    return "yes"


T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    # ///////////////////////////////////////////////////////////////////////////////////
    N = int(input())
    graph = []

    for i in range(N):
        tmp = input()
        graph.append(tmp)

    square = deque()
    for i in range(N):
        for j in range(N):
            if graph[i][j] == "#":
                square.append((i, j))

    answer = view(square, graph)
    print("#{} {}".format(test_case, answer))