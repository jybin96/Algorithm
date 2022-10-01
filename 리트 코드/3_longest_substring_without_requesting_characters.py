import collections

S = str(input())

result = []
length_max = 0

## 내풀이 O(n2제곱)
# for char in S:
#     if char not in result:
#         result.append(char)
#     else:
#         length_max = max(length_max, len(result))
#         result = result[result.index(char):]
#
# print(length_max)

## 해쉬를 사용한 해답 O(n)
used = {}
max_length = start = 0
for index, char in enumerate(S):
    if char in used and start <= used[char]:
        start = used[char] + 1
    else:
        max_length = max(max_length, index - start + 1)

    used[char] = index

print(max_length)




