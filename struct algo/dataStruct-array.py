### creating an 1D array

array = [x for x in range(0,11)]
#[0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(array)



###traversing 1D array

for i in range(len(array)):
    print(i,end=" ")

print("")
###get from array 
def getArr(arr,index):
    return arr[index]

print(getArr(array,-1))

### inserting into an index number without built in function
def insertArr(arr,value,index):
    arr[index] = value
    return arr
print(insertArr(array,5,2))

def delArr(arr,index):
    arr[index] = 0
    return arr

print(delArr(array,5))