current_passengers = 0
max_passengers = 0

for _ in range(10):
    data = list(map(int, input().split()))
    get_off_passengers = data[0]
    get_on_passengers = data[1]
    current_passengers = current_passengers - get_off_passengers + get_on_passengers
    if current_passengers > max_passengers:
        max_passengers = current_passengers
print(max_passengers)