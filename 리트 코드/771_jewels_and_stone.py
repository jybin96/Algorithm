J = str(input())
ST = str(input())

hashMap = {}
result = 0

for char in ST:
    if char not in hashMap:
        hashMap[char] = 1
    else:
        hashMap[char] += 1

print(hashMap)

for char in J:
    if char in hashMap:
        result += hashMap[char]

print(result)