import sys

def match(full, s):
  print full
  print s

def tryout(f, full, s, xmul, ymul, zmul):
  # Try out this mine with each column order
  # xyz
  xoff = f[0] - (s[0][0] * xmul)
  yoff = f[1] - (s[0][1] * ymul)
  zoff = f[2] - (s[0][2] * zmul)
  t = s[0:]
  print "offsets:", xoff, yoff, zoff
  t2 = []
  for l in t:
    x = (l[0] - xoff) * xmul
    y = (l[1] - yoff) * ymul
    z = (l[2] - zoff) * zmul
    t2.append([x, y, z])
  match(full, t2)

scanners = []
s = -1
fp = open("test.txt", 'r')
for line in fp:
  line = line.strip()
  if len(line) == 0:
    continue
  if '---' in line:
    s += 1
    scanners.append([])
    continue
  x,y,z = line.split(',')
  scanners[s].append([int(x), int(y), int(z)])

full = scanners[0]
unknown = len(scanners) - 1

while unknown > 0:
  for s in scanners[1:]:
    for f in full:
      for x_mul in [-1, 1]:
        for y_mul in [-1, 1]:
          for z_mul in [-1, 1]:
            print f
            print "and", s, x_mul, y_mul, z_mul
            tryout(f, full, s, x_mul, y_mul, z_mul)
            sys.exit()
