import sys

def dict_add(d, e, a):
  if e not in d:
    d[e] = []
  d[e].append(a)

m = []

fp = open("input.txt", 'r')
for line in fp:
  line = line.strip()
  m.append([int(x) for x in line])

paths = {}

dict_add(paths, 0, [[0, 0]])

while True:
  c = min(paths.keys())
  print c, len(paths[c])
  for p in paths[c]:
    if p[-1] == [len(m) - 1, len(m[0]) - 1]:
      print c, p
      sys.exit(0)
    # Add cheapest next step to cheapest path
    lr, lc = p[-1]
    if lr > 0 and m[lr -1][lc] != False:
      nd = p[0:]
      nd.append([lr - 1, lc])
      dict_add(paths, c + m[lr - 1][lc], nd)
      m[lr - 1][lc] = False
    if lr < len(m) - 1 and m[lr + 1][lc] != False:
      nd = p[0:]
      nd.append([lr + 1, lc])
      dict_add(paths, c + m[lr + 1][lc], nd) 
      m[lr + 1][lc] = False
    if lc > 0 and m[lr][lc - 1] != False:
      nd = p[0:]
      nd.append([lr, lc - 1])
      dict_add(paths, c + m[lr][lc - 1], nd)
      m[lr][lc - 1] = False 
    if lc < len(m[lr]) - 1 and m[lr][lc + 1] != False:
      nd = p[0:]
      nd.append([lr, lc + 1])
      dict_add(paths, c + m[lr][lc + 1], nd)
      m[lr][lc + 1] = False
  del paths[c]


