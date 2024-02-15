n = input()

ans = ""

for i in n:
    if n.index(i) % 2 != 0:
        ans = ans + i

print(ans)
