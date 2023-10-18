#Define a function which takes as a parameter dictionary and returns a dictionary in which everse the key-value pairs are reversed.
def reverse_dict(my_dict):
    reversed = {}
    for key, value in my_dict.items():
        reversed[value] = key
    return reversed
        
my_dict = {'a': 1, 'b': 2, 'c': 3}
print(reverse_dict(my_dict))
