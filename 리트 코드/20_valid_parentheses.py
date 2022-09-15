s = str(input())
stack = []
table = {
    ')': '(',
    '}': '{',
    ']': '['
}
print(not stack)
for char in s:
    if char not in table:
        stack.append(char)
    # 예외처리 - 스택이 비워져있는걸 체크하지않고 pop을 하게되면 오류걸린다.
    elif not stack or table[char] != stack.pop():
        print(False)
        break
print(len(stack) == 0)
