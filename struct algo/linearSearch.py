array = [3, 4, 5, 6, 7, 8, 9]
target = 8
for i in range(len(array)):
    if target == array[i]:
        print("Match found at: " + str(i))