#Define a function with takes two dictionaries as parameters and merge them and sum the values of common keys.
dict1 = {'a': 1, 'b': 2, 'c': 3}
dict2 = {'b': 3, 'c': 4, 'd': 5}

def merge_dicts(dict1, dict2):
    new_dict = dict1.copy()
    for keys, value in dict2.items():
        new_dict[keys] = new_dict.get(keys, 0) + value
    return new_dict
        
print(merge_dicts(dict1, dict2))
