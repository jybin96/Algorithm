def get_fibonacci(position):
    before_num = 0
    after_num = 1
    fibonacci_num = 0
    if position == 0:
        print(before_num)
    elif position == 1:
        print(after_num)
    else:
        for _ in range(position-1):
            fibonacci_num = before_num + after_num
            before_num = after_num
            after_num = fibonacci_num
        print(fibonacci_num)


n = int(input())
get_fibonacci(n)
