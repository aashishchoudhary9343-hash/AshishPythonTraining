import math
a, b, c = map(int, input("Enter three numbers: ").split())
maximum = a if (a >= b and a >= c) else (b if b >= c else c)
print("Maximum of the three numbers =", maximum)