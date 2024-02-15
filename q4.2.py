n = int(input())
if n < 60:
    c = 60 - n
    print(
        "Sorry!, Not Eligible for Addimision you need {} more marks to take addmission".format(
            c
        )
    )
else:
    print("You are eligible for admission")
