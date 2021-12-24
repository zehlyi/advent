import sys

def dict_add(d, x, c):
  if x not in d:
    d[x] = 0
  d[x] += c

def do_sum(p, b):
  d = {}
  for k in p.keys():
    dict_add(d, k[0], p[k])
  dict_add(d, b, 1)
  print d
  return d

polymer = []
poly = {}
d = {}

fp = open("input.txt", 'r')
for line in fp:
  line = line.strip()
  if len(line) == 0: 
    continue
  if '>' in line:
    x, y = line.split(' -> ')
    d[x] = y
    continue
  polymer = line

for i in range(len(polymer) - 1):
  p = "".join(polymer[i:i+2])
  dict_add(poly, p, 1)

print poly

for s in range(10):
  poly2 = {}
  for p in poly.keys():
    if p in d:
      dict_add(poly2, "".join([p[0], d[p]]), poly[p])
      dict_add(poly2, "".join([d[p], p[1]]), poly[p])

  poly = poly2
  print poly
  print sum(poly.values()) + 1
  totals = sorted(do_sum(poly, polymer[-1]).values())
  print totals[-1] - totals[0]

