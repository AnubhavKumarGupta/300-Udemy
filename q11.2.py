print("Input 1st number")

a = int(input())

print("input 2nd number")

b = int(input())

print("Input 3rd number")

c = int(input())


# 1st method

# print(max(a, b, c))

# 2nd method

# if a > b and a > c:
#     print(a)
# elif b > c and b > a:
#     print(b)
# else:
#     print(c)


# 3rd method

d = a if a > b and a > c else b>a and b > c 
print("The largest of the three numbers is", d)
