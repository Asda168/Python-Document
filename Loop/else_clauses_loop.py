for i in range(2, 10):
    for j in range(2, i):
        if i % j == 0:
            print(f"{i} is divisible by {j}")
            break
    else:
        print(f"{i} is a prime number")