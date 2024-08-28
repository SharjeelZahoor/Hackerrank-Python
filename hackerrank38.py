from itertools import permutations
S, k = input().split()
for i in sorted(list(permutations(S, int(k)))):
    print("".join(i))
