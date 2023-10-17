def linear_search(arr, key):
    for i in arr:
        if i == key:
            return "Found"
    return "Not found"
my_array = range(1,11)
num = 10
print(linear_search(my_array,num))
