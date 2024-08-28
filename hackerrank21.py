def average(array):
    # your code goes here
    res=0
    for i in set(array):
        res=res+i
    average = (res)/len(set(array))
    return average

if __name__ == '__main__':
    n = int(input())
    arr = list(map(int, input().split()))
    result = average(arr)
    print(result)
