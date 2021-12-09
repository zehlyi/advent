import sys

fp = open("test.txt", 'r')

tree = {}
for line in fp:
  bits = line.strip()
  t = tree
  for c in range(len(bits)-1):
    b = int(bits[c])
    if b not in t:
      t[b] = {}
    t = t[b]
  b = int(bits[len(bits)-1])
  if b not in t:
    t[b] = 0
  t[b] += 1



print tree  
