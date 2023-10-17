#Write a function to find all pairs of an integer array whose sum is equal to a given number. Do not consider commutative pairs.
def pair_sum(myList, sum):
    output = []
    for i in range(len(myList)):
        for j in range(i+1,len(myList)):
            if (myList[i]+myList[j]==sum) and ((str(myList[i])+'+'+str(myList[j]) not in output)) and ((str(myList[j])+'+'+str(myList[i])) not in output):
                output.append(str(myList[i])+'+'+str(myList[j]))
    return output
print(pair_sum([2, 4, 3, 5, 6, -2, 4, 7, 8, 9],7))
