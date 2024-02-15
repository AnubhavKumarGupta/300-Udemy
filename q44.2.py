m = int(input())
n = int(input())

l = []
for x in range(m, n, -1):
    l.append(x)

print(l)
print(sum(l))
