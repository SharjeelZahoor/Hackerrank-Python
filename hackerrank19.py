def print_rangoli(size):
    n = size
    li = list(map(chr, range(97, 123)))
    x = li[n-1::-1] + li[1:n]
    m = len('-'.join(x))
    for i in range(1, n):
        print('-'.join(li[n-1:n-i:-1]+li[n-i:n]).center(m,'-'))
    for i in range(n, 0, -1):
        print("-".join(li[n-1:n-i:-1]+li[n-i:n]).center(m,'-'))
if __name__ == '__main__':
    n = int(input())
    print_rangoli(n)