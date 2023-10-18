#Define a function to count the frequency of words in a given list of words.
def count_word_frequency(words):
    frequency = {}
    for word in words:
        if word in frequency:
            frequency[word] += 1
        else:
            frequency[word] = 1
    return frequency
print(count_word_frequency(['apple', 'orange', 'banana', 'apple', 'orange', 'apple']))
print(count_word_frequency([]))
print(count_word_frequency(['apple']))
