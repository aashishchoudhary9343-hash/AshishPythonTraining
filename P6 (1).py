def rev(x):
    return int(str(x)[::-1])

N = int(input())
for _ in range(N):
    a, b = map(int, input().split())
    ans = rev(rev(a) + rev(b))
    print(ans)