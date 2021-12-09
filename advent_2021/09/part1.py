import sys

floor = []
fp = open("input.txt", 'r')
for line in fp:
  floor.append(line.strip())

total = 0
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
    total += int(floor[r][c]) + 1
print "total", total  
