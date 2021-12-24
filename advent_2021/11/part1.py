import sys

def update_neighbors(r, c, rows, cols, o):
  for i in range(max(0, r-1), min(rows, r+2)):
    for j in range(max(0, c-1), min(cols, c+2)):
      if o[i][j] != 0:
        o[i][j] += 1

def print_o(o):
  for r in o:
    print r

o = []
fp = open("input.txt", 'r')
for line in fp:
  line = line.strip()
  tmp = []
  for c in line:
    tmp.append(int(c))
  o.append(tmp)

rows = len(o)
cols = len(o[0])

flashes = 0
for s in range(1, 101):
  #print "step: ", s
  for r in range(rows):
    for c in range(cols):
      o[r][c] += 1
  while True:
    new_flashes = 0
    for r in range(rows):
      for c in range(cols):
        if o[r][c] > 9:
          # Flash!
          new_flashes += 1
          o[r][c] = 0
          update_neighbors(r, c, rows, cols, o)
    flashes += new_flashes
    #print_o(o)
    #print "new flashes: ", new_flashes
    if new_flashes == 0:
      break
  print "At end of step", s, "we have seen", flashes, "flashes"
  print_o(o)
