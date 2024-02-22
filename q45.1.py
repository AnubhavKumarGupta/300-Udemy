m = int(input())
n = int(input())

l = []
for x in range(m, n, 2):
    l.append(x)

print("first-way", l)

print()

print("Second-way", list(y for y in range(m, n) if y % 2 != 0))  # list comprehension
