a = int(input())
b = int(input())

s = input()


def fn(a, b):
    if s == "+":
        print(a + b)
    elif s == "-":
        print(a - b)
    elif s == "*":
        print(a * b)
    elif s == "/":
        print(a / b)
    else:
        print("Invalid operator")


fn(a, b)
