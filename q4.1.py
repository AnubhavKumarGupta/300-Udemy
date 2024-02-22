n = int(input())
if n < 18:
    print(
        "You are not eligible to vote, You Will be able to Participate after {c} Years".format(
            c=18 - n
        )
    )
else:
    print("You are eligible to vote")
