def find_max_min(num_list):
    min_v = num_list[0]
    max_v = num_list[0]
    for i in range(1, len(num_list)):
        if min_v > num_list[i]:
            min_v = num_list[i]
        if max_v < num_list[i]:
            max_v = num_list[i]
    print(min_v, max_v)


N = int(input())
num_list = list(map(int, input().split()))
find_max_min(num_list)