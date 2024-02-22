m = int(input())
n = int(input())

# l = []
# for x in range(m, n, 3):
#     l.append(x)

# print(l)

print(list(y for y in range(m, n) if y % 2 != 0))
