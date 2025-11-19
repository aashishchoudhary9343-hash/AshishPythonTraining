n = int(input())
for _ in range(n):
    SH, SM, EH, EM = map(int, input().split())
    
    if EM < SM:
        EM += 60
        EH -= 1
    
    print(EH - SH, EM - SM)
