
# Enter your code here. Read input from STDIN. Print output to STDOUT
total_stamps = int(input())
countries = set()

for i in range(total_stamps):
    countries.add(input())
print(len(countries))
