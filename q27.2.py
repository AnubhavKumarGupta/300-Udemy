list = eval(input())
l = []
for x in list:
    if x % 4 == 0 and x % 100 != 0 or x % 400 == 0:
        l.append(x)

print("the following is Leap Year", l)
