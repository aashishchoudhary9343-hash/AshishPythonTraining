amount = int(input().strip())
start = int(input().strip())

denoms = [100, 50, 20, 10, 5, 2, 1]

start_index = denoms.index(start)

for d in denoms[start_index:]:
    count = amount // d
    print(f"{d} rupees note: {count}")
    amount %= d