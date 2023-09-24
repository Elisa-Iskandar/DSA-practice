a = [-2, -3, 4, -1, -2, 1, 5, -3]
def kadane(a, size):
  current_max = a[0]
  global_max = a[0]
  for x in range(size):
    #print([x])
    current_max = max(a[x],current_max+a[x])
    #print(current_max)
    if current_max > global_max:
        global_max = current_max
    #print(global_max)
  return global_max

print(kadane(a,len(a)))
