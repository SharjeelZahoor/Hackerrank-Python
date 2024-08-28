def mutation():
    opr = input().split()
    operation = opr[0]
    s3 = list(map(int, input().split()))
    if operation == "intersection_update":
        s1.intersection_update(s3)
    elif operation == "update":
        s1.update(s3)
    elif operation == "symmetric_difference_update":
        s1.symmetric_difference_update(s3)
    elif operation == "difference_update":
        s1.difference_update(s3)
    return sum(s1)

a = int(input())
s1 =set(map(int, input().split()))
n = int(input())
for i in range(n-1):
    mutation()
print(mutation())