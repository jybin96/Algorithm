import collections
import time


def isPalindrome(data) -> bool:
    while len(data) > 1:
        if data.popleft() != data.pop():
            return False
    return True

start = time.time()
# 리스트로 변환 풀이법
str_data = collections.deque([
    char.lower() for char in str(input())
    if char.isalnum()
])

print(isPalindrome(str_data))
end = time.time()
print(f"{end - start:.5f} sec")

