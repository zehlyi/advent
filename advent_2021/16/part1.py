import sys

def parse_literal(b, c):
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
  return c

def parse(b, c, vs):
  print "Parse:", c, b[c:]
  if c >= len(b):
    return c
  # Version
  vers = int(b[c:c+3], 2)
  c += 3
  vs[0] += vers
  # Type
  t = int(b[c:c+3], 2)
  c += 3
  print "vers:", vers, "type:", t
  if t == 4:
    # Literal
    c = parse_literal(b, c)
  else:
    # op
    i = b[c]
    c += 1
    if i == '0':
      # next 15b are length
      length = int(b[c:c+15], 2)
      c += 15
      print "length", length
      c_end = c + length
      while c < c_end:
        c = parse(b, c, vs)
    else:
     # next 11b are count
     count = int(b[c:c+11], 2)
     c += 11
     print "count", count
     x = 0
     while x < count:
       c = parse(b, c, vs)
       x += 1
  return c


fp = open("input.txt", 'r')
for line in fp:
  line = line.strip()

#line = 'D2FE28'
#line = '38006F45291200'
#line = 'EE00D40C823060'
#line = '620080001611562C8802118E34'
#line = 'C0015000016115A2E0802F182340'
#line = 'A0016C880162017C3686B18A3D4780'

b = []
for h in line:
  b.append(bin(int(h, 16))[2:].zfill(4))

b = "".join(b)
print b

vs = [0]
print parse(b, 0, vs)
print "Version sum", vs[0]

