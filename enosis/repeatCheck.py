number = []
repeat = []

n = int(input("Total number: "))

for i in range(n):
    x = input("Number {}:".format(i+1))
    if x in number:
        repeat.append(x)
    else:
        number.append(x)


print("Repeat value:{}"," ".join(repeat))