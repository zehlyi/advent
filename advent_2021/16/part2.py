import sys

def parse_literal(b, c, lits):
  l = []
  while b[c] == '1':
    c += 1
    l.append(b[c:c+4])
    c += 4
  c += 1
  l.append(b[c:c+4])
  c += 4
  l = "".join(l)
  lit = int(l, 2)
  print "Literal:", lit
  lits.append(lit)
  return c

def parse(b, c, vs):
  print "Parse:", c, b[c:]
  if c >= len(b):
    return c
  # Version
  vers = int(b[c:c+3], 2)
  c += 3
  # Type
  t = int(b[c:c+3], 2)
  c += 3
  if t == 4:
    # Literal
    c = parse_literal(b, c, vs)
  else:
    # op
    i = b[c]
    c += 1
    lits = []
    if i == '0':
      # next 15b are length
      length = int(b[c:c+15], 2)
      c += 15
      print "length", length
      c_end = c + length
      while c < c_end:
        c = parse(b, c, lits)
    else:
     # next 11b are count
     count = int(b[c:c+11], 2)
     c += 11
     print "count", count
     x = 0
     while x < count:
       c = parse(b, c, lits)
       x += 1
    print "After op, lits is", lits
    ret = 0
    if t == 0:
      ret = sum(lits)
    if t == 1:
      ret = 1
      for val in lits:
        ret *= val
    if t == 2:
      ret = min(lits)
    if t == 3:
      ret = max(lits)
    if t == 5:
      ret = 1 if lits[0] > lits[1] else 0
    if t == 6:
      ret = 1 if lits[0] < lits[1] else 0
    if t == 7:
      ret = 1 if lits[0] == lits[1] else 0
    vs.append(ret)
  return c


fp = open("input.txt", 'r')
for line in fp:
  line = line.strip()

#line = 'C200B40A82'
#line = '04005AC33890'
#line = '880086C3E88112'
#line = 'CE00C43D881120'
#line = 'D8005AC2A8F0'
#line = 'F600BC2D8F'
#line = '9C005AC2F8F0'
#line = '9C0141080250320F1802104A08'

b = []
for h in line:
  b.append(bin(int(h, 16))[2:].zfill(4))

b = "".join(b)
print b

vs = []
print parse(b, 0, vs)
print vs

