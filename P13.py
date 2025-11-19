N = int(input())

total_stones = 0
i = 1

while True:
    # Ramesh's turn
    if total_stones + i >= N:
        print("Ramesh")
        break
    total_stones += i

    # Suresh's turn
    if total_stones + 2*i >= N:
        print("Suresh")
        break
    total_stones += 2*i

    i += 1
