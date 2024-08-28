A = set(input().split())
num_sets = int(input())
is_superset = True

for i in range(num_sets):
    B = set(input().split())
    if not A.issuperset(B):
        is_superset = False
        break

print(is_superset)



