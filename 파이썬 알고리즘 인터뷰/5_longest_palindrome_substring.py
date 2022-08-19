def expand(left: int, right: int, string: str) -> str:
    while left >= 0 and right < len(string) and string[left] == string[right]:
        left -= 1
        right += 1
    return string[left + 1:right]


string = str(input())
result = ""
if len(string) < 2 or string == string[::-1]:
    result = string
    print(result)
else:
    for i in range(len(string) - 1):
        result = max(result, expand(i, i + 2, string), expand(i, i + 1, string), key=len)
    print(result)
