import sys

def enhance(key, m, default):
  #for i in m:
  #  print "".join(i)
  #print "default now", default
  m_out = []
  for i in range(len(m)):
    m_out.append(['.'] * len(m[0]))
  for i in range(len(m)):
    for j in range(len(m[i])):
      ind = ""
      for x in [-1, 0, 1]:
         for y in [-1, 0, 1]:
           if i+x < 0 or i+x >= len(m) or j+y < 0 or j+y >= len(m[i]):
             ind += default[0]
           else:
             ind += "1" if m[i+x][j+y] == "#" else "0"
      ind = int(ind, 2)
      m_out[i][j] = key[ind]
  for i in m_out:
    print "".join(i)
  default[0] = '1' if m_out[0][0] == "#" else '0'
  #print "Default at end", default
  print
  return m_out

key = []
m = []
fp = open("input.txt", 'r')
for line in fp:
  line = line.strip()
  if len(key) == 0:
    key = line
    continue
  if len(line) == 0:
    continue
  m.append('.' * 100 + line + '.' * 100)

m = ['.' * len(m[0])]*100 + m + ['.' * len(m[0])]*100

#print key
#print m
default = ['0']
for s in range(50):
  m = enhance(key, m, default)

c = 0
for i in m:
  for j in i:
    if j == "#":
      c += 1
print c
