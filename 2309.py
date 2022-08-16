import itertools

def init_dwarf():
    dwarf_list = []
    for _ in range(9):
        dwarf_list.append(int(input()))
    return dwarf_list

def find_seven_dwarf(list):
    dwarf_tuple = ()
    for real_dwarf_tuple in itertools.combinations(list, 7):
        if sum(real_dwarf_tuple) == 100:
            dwarf_tuple = real_dwarf_tuple

    for real_dwarf in sorted(dwarf_tuple, key=lambda x: x):
        print(real_dwarf)

find_seven_dwarf(init_dwarf())
