#Find the maximum product of two integers in an array where all elements are positive.
def max_product(arr):
    max = -1
    for i in range(len(arr)):
        for j in range(i+1,len(arr)):
            if arr[i]*arr[j]>max:
                max = arr[i]*arr[j]
    return max
arr = [1, 7, 3, 4, 9, 5] 
max_product(arr)
print(max_product(arr))
