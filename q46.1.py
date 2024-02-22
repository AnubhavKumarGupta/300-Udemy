import math as m

print("Hi there, Tell me you name")

name = input()

print("The Name is", name)

score = eval(input())

print("Your Total Marks is", sum(score))

print("Your English Marks is", score[0])
print("Your Hindi Marks is", score[1])
print("Your Math Marks is", score[2])
print("Your Science Marks is", score[3])
print("Your SST Marks is", score[4])
print("Your Average is", (sum(score) // 5))
