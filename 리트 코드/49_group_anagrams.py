import collections

str_list = list(map(str, input().split()))
str_dic = collections.defaultdict(list)

print(str_list)
for string in str_list:
    str_dic["".join(sorted(string))].append(string)

print(list(str_dic.values()))
