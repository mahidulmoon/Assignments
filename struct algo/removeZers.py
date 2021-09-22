array = [0,1,3,0,12]


def removeZero():
    current = 0
    for i in range(len(array)-1):
        if array[i] != 0:
            array[current] = array[i]
            current = current + 1
    for i in range(current,len(array)-1):
        array[i] = 0
    return array

print("Remove Zero Result: ",removeZero())