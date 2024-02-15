import math as m

a = int(input())
b = int(input())
c = int(input())

d = b**2 - 4 * a * c

if d > 0:
    e = (-b + m.sqrt(d)) // 2 * a
    print(e)
    f = (-b - m.sqrt(d)) // 2 * a
    print(f)

elif d == 0:
    g = (-b + m.sqrt(d)) // 2 * a
    print(g)

else:
    print("No Roots")
