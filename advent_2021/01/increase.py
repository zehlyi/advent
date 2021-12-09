import sys

fp = open("input1.txt", 'r')

lc = 0
p = -1
pp = -1
ppp = -1
c = 0
s = 0
o = 0
for line in fp:
  d = int(line.strip())
  if lc == 0:
    o = -1
    s = d
    print("%d n/a" % d)
    pass
  if lc == 1:
    o = p
    s = p + d
  if lc == 2:
    o = pp + p
    s = pp + p + d
  if lc > 2:
    o = ppp + pp + p
    s = pp + p + d
    if (ppp + pp + p) < (pp + p + d):
      c += 1
  print("old sum: %d; new sum: %d; count: %d" % (o, s, c))
  # clean up
  lc += 1
  ppp = pp
  pp = p
  p = d
  
print("count: %d" % c)
