import sys

energy = {'A': 1, 'B' : 10, 'C' : 100, 'D' : 1000}
homes = {'A' : [[3, 3], [2, 3]], 'B' : [[3, 5], [2, 5]], 'C' : [[3, 7], [2, 7]], 'D' : [[3, 9], [2, 9]]}

seen_maps = {}

def HashEm(m):
  s = ""
  for l in range(1, len(m) - 1):
    s += "".join(m[l])
  return s

def BestSeen(all_maps, m, cost):
  h = HashEm(m)
  if h not in seen_maps:
    seen_maps[h] = cost
    return True
  if seen_maps[h] <= cost:
    return False
  if seen_maps[h] in all_maps:
    all_maps[seen_maps[h]].remove(m)
  seen_maps[h] = cost
  return True    

def PrintMap(m):
  for l in m:
    print "".join(l)
  print

def NewMap(m):
  new = []
  for l in m:
    new.append(l[0:])
  return new

def AddMapToDict(d, m, c):
  if not BestSeen(d, m, c):
    return
  if c not in d:
    d[c] = []
  if m not in d[c]:
    d[c].append(m)

def CanMoveToCol(m, nr, nc, gc):
  if m[nr][gc] != '.':
    return False
  while nc != gc:
    nc += 1 if gc > nc else -1
    if m[nr][nc] != '.':
      return False
  return True
      
def CanMoveToRow(m, nr, nc, gr):
  if m[gr][nc] != '.':
    return False
  while nr != gr:
    nr += 1 if gr > nr else -1
    if m[nr][nc] != '.':
      return False
  return True

def MoveCost(r, col, nr, nc, a):
  return (abs(r - nr) + abs(col - nc)) * energy[a]

def GetHome(m, c):
  for h in homes[c]:
    hr, hc = h
    if m[hr][hc] != c:
      return h

def IsSolved(m):
  for c in homes:
    for h in homes[c]:
      hr, hc = h
      if m[hr][hc] != c:
        return False
  return True

def MoveToRoom(m):
  cost = 0
  r = 1
  for col in range(1, len(m[r]) - 1):
    c = m[r][col]
    if c >= 'A' and c <= 'D':
      # Try to move into a room if we're in the hall
      hr, hc = GetHome(m, c)
      if CanMoveToCol(m, r, col, hc) and CanMoveToRow(m, r, hc, hr):
        m[r][col] = '.'
        m[hr][hc] = c
        cost += MoveCost(r, col, hr, hc, c)
  return cost

def MoveToHall(all_maps, m, mcost):
  for r in [2, 3]:
    for col in range(len(m[r])):
      c = m[r][col]
      if c >= 'A' and c <= 'D':
        h = GetHome(m, c)
        if not h or (h[0] == r and h[1] == col):
          pass
        # Hall is row 1
        if CanMoveToRow(m, r, col, 1):
          # Can we move somewhere not above a home
          for ok_col in [1, 2, 4, 6, 8, 10, 11]:
            if ok_col != col and CanMoveToCol(m, 1, col, ok_col):
              # It can work! Add to list of maps
              cost = mcost + MoveCost(r, col, 1, ok_col, c)
              new_map = NewMap(m)
              new_map[r][col] = '.'
              new_map[1][ok_col] = c
              # If we can move anyting to its house, we always want to.
              nc = MoveToRoom(new_map)
              cost += nc
              while nc > 0:
                nc = MoveToRoom(new_map)
                cost += nc
              AddMapToDict(all_maps, new_map, cost)
 
m = []
all_maps = {}
fp = open("input.txt", 'r')
for line in fp:
  l = []
  for c in line[:-1]:
    l.append(c)
  m.append(l)

AddMapToDict(all_maps, m, 0)

cheapest = -1
while True:
  cheapest += 1
  # Pop cheapest set of maps
  if cheapest not in all_maps:
    continue
  print cheapest
  for m in all_maps[cheapest]:
    if IsSolved(m):
      PrintMap(m)
      print "Found it!"
      print cheapest
      sys.exit()
 
    MoveToHall(all_maps, m, cheapest)

  del all_maps[cheapest]
