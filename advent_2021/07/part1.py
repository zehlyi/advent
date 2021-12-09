import sys

crabs = {}

fp = open("input.txt", 'r')
for line in fp:
  f = line.strip().split(',')
  f = [int(x) for x in f]
  for x in f:
    if not x in crabs:
      crabs[x] = 0
    crabs[x] += 1

print crabs

min_dist = 1000000000
for i in range(max(crabs.keys())):
  dist = 0
  for k in crabs.keys():
    dist += abs(k - i) * crabs[k]
  print("For pos %d, total dist is: %d" % (i, dist))
  if dist > min_dist:
    break
  if dist < min_dist:
    min_dist = dist

print min_dist
 
