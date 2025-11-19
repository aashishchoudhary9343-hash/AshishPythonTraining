N = int(input().strip())
X = int(input().strip())

for _ in range(N):
    Y = int(input().strip())
    if Y >= X:
        print("YES")
    else:
        print("NO")