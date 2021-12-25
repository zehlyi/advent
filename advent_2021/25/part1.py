import sys

def print_map(c):
  for l in c:
    print "".join(l)
  print

def move_west(c, c2):
  moves = 0
  for j in range(len(c)):
    for i in range(len(c[j])):
      s = c[j][i]
      if s == '>':
        ni = (i + 1) % len(c[j])
        if c[j][ni] == '.':
          c2[j][ni] = '>'
          moves += 1
        else:
          c2[j][i] = '>'
      elif s == 'v':
        c2[j][i] = 'v'
  return moves

def move_south(c, c2):
  moves = 0
  for j in range(len(c)):
    for i in range(len(c[j])):
      s = c[j][i]
      if s == 'v':
        nj = (j + 1) % len(c)
        if c[nj][i] == '.':
          c2[nj][i] = 'v'
          moves += 1
        else:
          c2[j][i] = 'v'
      elif s == '>':
        c2[j][i] = '>'
  return moves

def take_step(c):
  c2 = []
  c3 = []
  for j in range(len(c)):
    c2.append(['.'] * len(c[0]))
    c3.append(['.'] * len(c[0]))

  moves = move_west(c, c2)
  moves += move_south(c2, c3)
  if moves == 0:
    sys.exit()
  return c3
 


cukes = []

f = open('input.txt', 'r')
for line in f:
  cukes.append([x for x in line.strip()])

print_map(cukes)

steps = 0
while True:
  steps += 1
  print steps
  new_cukes = take_step(cukes)
  #print_map(new_cukes)
  cukes = new_cukes
