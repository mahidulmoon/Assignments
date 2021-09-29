value = [
    [1,2,3],
    [4,5,6],
    [7,8,9]
]


def rotate(matrix):
    list_of_tuples = zip(*matrix[::-1])
    return [list(elem) for elem in list_of_tuples]


print("Data: ",rotate(value))