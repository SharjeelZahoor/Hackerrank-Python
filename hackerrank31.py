T = int(input())
for i in range(T):
    a = int(input())
    sa = set(input().split())
    b = int(input())
    sb = set(input().split())
    print(sa.issubset(sb))



