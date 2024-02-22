n = int(input())

for i in range(n + 1):
    for j in range(i + 1):
        print(chr(64 + i) * j)
    print()
