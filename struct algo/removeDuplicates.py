value = [1,2,3,4,4,5,7,3,8,9]


def removeDuplicates(arr):
    # if(len(arr) == 0):
    #     return 0
    # i = 0
    # for j in range(0,len(arr)):
    #     if(arr[i] != arr[j]):
    #         arr[i] = arr[j]
    # return i+1
    newValue = set(arr)
    return list(newValue)


print("value: ",removeDuplicates(value))