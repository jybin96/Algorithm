import collections


class MyStack:
    def __init__(self):
        self.q = collections.deque()

    # deque 에서는 stack의 기능인 pop이 존재한다 하지만 문제 자체에서 큐로 스택을 구현하라고 하였으니 큐의 연산자인 popleft로 풀이하였다.
    def push(self, value):
        self.q.append(value)
        for _ in range(len(self.q) - 1):
            self.q.append(self.q.popleft())

    def pop(self):
        return self.q.popleft()

    def top(self):
        return self.q[0]

    def empty(self):
        return len(self.q) == 0


stack = MyStack()
stack.push(1)
stack.push(2)
print(stack.top())
print(stack.pop())
print(stack.empty())

