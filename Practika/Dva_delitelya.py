def check_divisibility(n):
    for i in range(1, n + 1):
        if i % 2 == 0 and i % 4 != 0:
            print(f"{i} - Делится на 2, но не на 4")
        elif i % 4 == 0:
            print(f"{i} - Делится и на 2, и на 4")
        else:
            print(i)

check_divisibility(10)