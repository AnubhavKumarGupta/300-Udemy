lst = ["pink", "2323", "dsfasdgas", "154fx", "898bdsf"]
for i in lst:
    if i != lst[0] and i != lst[-1] and len(i) != 5:
        print(i)
