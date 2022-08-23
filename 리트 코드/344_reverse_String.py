str_list = [char for char in str(input())]
str_list.reverse()
print(str_list)


# two pointer use
def reverseString(s: [str]) -> None:
    left, right = 0, len(s) - 1
    while left < right:
        s[left], s[right] = s[right], s[left]
        left += 1
        right -= 1
