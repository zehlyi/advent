fp = open("input.txt", 'r')

a = {}
s_x = r_x = 0
s_y = r_y = 0
a[0] = {}
a[0][0] = 1 #starting house
turn = 0

for line in fp:
  for c in line.strip():
    if turn == 0:
      x = s_x
      y = s_y
    else:
      x = r_x
      y = r_y

    if c == '>':
      x += 1
    elif c == '<':
      x -= 1
    elif c == '^':
      y += 1
    elif c == 'v':
      y -= 1
    else:
      print "ERROR"
        
    if not x in a:
      a[x] = {}
    if not y in a[x]:
      a[x][y] = 0 
    a[x][y] += 1

    if turn == 0:
      s_x = x
      s_y = y
      turn = 1
    else:
      r_x = x
      r_y = y
      turn = 0
    

print sum([len(a[x].keys()) for x in a])
    
