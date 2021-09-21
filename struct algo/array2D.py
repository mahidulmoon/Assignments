array = [
    [1,2],
    [3,4],
    [5,6],
]

def getValue(arr,r,c):
    return arr[r][c]
#getting value
print(getValue(array,1,1))

#adding value
array.insert([3][0],[10,20])
print(array)

#updating value
array[2][1] = 100
print(array)


#2D array traversing
print("2D array traversing")
for i in range(len(array) -1):
    for j in range(len(array[0])-1):
        print(array[i][j])