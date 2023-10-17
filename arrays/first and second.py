#Given a list, write a function to get first, second best scores from the list.
#List may contain duplicates.
def first_second(my_list):
    first = -1
    second = -1
    for x in my_list:
        if first<=x: #allows for dupes!
            second = first
            first = x
    return first, second
myList = [84,85,86,87,85,90,85,83,23,45,84,1,2,0]
print(first_second(myList)) # 90 87
