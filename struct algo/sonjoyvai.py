n_ish = int(input("FIrst input: "))
counter_dict = {}
words_list = []

for i in range(n_ish):
    word = input("for loop input: "+str(i+1))
    words_list.append(word)

    if word in counter_dict:
        counter_dict[word] += 1
    else:
        counter_dict[word] = 1

print(len(counter_dict))
print(' '.join([str(counter_dict[word]) for word in counter_dict]))
