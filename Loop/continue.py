i = 2
j = 10

for number in range(i, j):
    # Check if number is divisible by 2
    if number % 2 == 0:
        print(f"Found an even number {number}")
        continue
    # If number is not divisible by 2, print it
    print(f"Found an odd number {number}")