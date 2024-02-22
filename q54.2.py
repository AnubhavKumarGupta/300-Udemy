def fn(a):
    if a == 1:
        return 1
    else:
        return a * fn(a - 1)


n = int(input())


print(fn(n))
