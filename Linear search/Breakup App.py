#accepted solution for hackerearth
n = int(input())
scores = [0, 0]
for x in range(n):
  temp = str(input())
  if temp[0] == 'G':
    scores[0] += temp.count('19')*2
    scores[1] += temp.count('21')*2  
  else:
    scores[0] += temp.count('19')
    scores[1] += temp.count('21')
if scores[0] > scores[1]:
  print("Date")
else:
  print("No Date")
