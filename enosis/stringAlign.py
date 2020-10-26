string = "I don't want the text to be in the center of my screen. I want it to be in the center of that 24 spaces. If I have to do it manually, what is the math behind adding the same no. of spaces before and after the text?"

s = True

for i in range(len(string)):
    if i%20 == 0:
        print(string[i])
    else:
        print(string[i],end="")
