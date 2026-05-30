i = 2
j = 10

for y in range(i, j):
    for x in range(i, y):
        if y % x == 0:
            print(f"{y} equals {x} * {int(y/x)}")
            break
    else:
        print(f"{y} is a prime number")