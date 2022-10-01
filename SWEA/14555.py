T = int(input())
for test_case in range(1, T + 1):
    land = str(input())
    count = 0
    for i in range(len(land)-1):
        first_pointer = land[i]
        second_pointer = land[i+1]
        if first_pointer + second_pointer == "(|":
            count += 1
        elif first_pointer + second_pointer == "|)":
            count +=1
        elif first_pointer + second_pointer == "()":
            count +=1
    print(f"#{test_case} {count}")