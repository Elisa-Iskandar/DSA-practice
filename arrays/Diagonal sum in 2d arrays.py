#Given 2D list calculate the sum of diagonal elements.
def diagonal_sum(matrix):
    sum = 0
    for rows in range(len(matrix)):
        for columns in range(len(matrix[0])):
            if rows == columns:
                sum += matrix[rows][columns]
    return sum
myList2D= [[1,2,3],[4,5,6],[7,8,9]] 
print(diagonal_sum(myList2D))
