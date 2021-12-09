import sys

def add_points(r, c, check):
  if r > 0:
    check.append([r-1, c])
  if r < len(floor) - 1:
    check.append([r+1, c])
  if c > 0:
    check.append([r, c-1])
  if c < len(floor[r]) - 1:
    check.append([r, c+1])

floor = []
fp = open("input.txt", 'r')
for line in fp:
  floor.append([x for x in line.strip()])

seeds = []
for r in range(len(floor)):
  for c in range(len(floor[r])):
    if r > 0 and floor[r][c] >= floor[r-1][c]:
      continue
    if r < len(floor) - 1 and floor[r][c] >= floor[r+1][c]:
      continue
    if c > 0 and floor[r][c] >= floor[r][c-1]:
      continue
    if c < len(floor[r]) - 1 and floor[r][c] >= floor[r][c+1]:
      continue
    print "Found mininum", floor[r][c]
    seeds.append([r, c])

basins = []
for [r1,c1] in seeds:
  curr_basin = 0
  print r1, c1
  check = []
  check.append([r1, c1])
  while len(check) > 0:
    [r, c] = check[0]
    check = check[1:]
    if floor[r][c] != '9':
      curr_basin += 1 
      add_points(r, c, check)
      floor[r][c] = '9'
  print "basin total:", curr_basin
  basins.append(curr_basin)

basins = sorted(basins)
print basins[-1] * basins[-2] * basins[-3]
