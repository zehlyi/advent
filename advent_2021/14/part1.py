import sys

poly = []
d = {}

fp = open("test.txt", 'r')
for line in fp:
  line = line.strip()
  if len(line) == 0: 
    continue
  if '>' in line:
    x, y = line.split(' -> ')
    d[x] = y
    continue
  poly = line

print poly
print d

for s in range(10):
  poly2 = []
  for i in range(len(poly)-1):
    poly2.append(poly[i])
    k = "".join(poly[i:i+2])
    if k in d:
      poly2.append(d[k])
  poly2.append(poly[-1])
  poly = poly2
  print "".join(poly)
  print len(poly)

