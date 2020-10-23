f = open('input.txt', 'r')
s = 0 
number = f.read()
for i in number.split(" "):
    s+=int(i)


of = open('output.txt','w')
of.write("sum is:{}".format(s))

f.close()
of.close()