f = open('input1.txt', 'r')
two_tags = 0
three_tags = 0
for line in f:
  twos = False
  threes = False
  tag = line.strip()
  d = {}
  for x in tag:
    if x not in d:
      d[x] = 0
    d[x] += 1

  for x in d:
    if d[x] == 2:
      twos = True
    if d[x] == 3:
      threes = True

  if twos:
    two_tags += 1
  if threes:
    three_tags += 1

print two_tags * three_tags

    
  
  
