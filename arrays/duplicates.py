#Write a function to remove the duplicate numbers on given integer array/list.
def remove_duplicates(arr):
    output = []
    for i in range(len(arr)):
        if arr[i] not in output:
            output.append(arr[i])
    return output
print(remove_duplicates([1, 1, 2, 2, 3, 4, 5]))
