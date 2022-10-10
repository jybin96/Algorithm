dic = {"MON": 6, "TUE" : 5, "WED": 4, "THU": 3, "FRI": 2, "SAT": 1, "SUN": 7}

T = int(input())
S_list = [input() for _ in range(T)]

for i, S in enumerate(S_list):
    print(f"#{i+1} {dic.get(S)}")