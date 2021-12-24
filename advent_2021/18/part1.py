import sys
import ast

def explode_help(t, n):
  if not isinstance(t, list):
    return False
  if n > 3:
    tmp = t[0:]
    print "exploding", tmp
    return tmp
  for tn in t:
    #print "explode left", t[1], n+1
    r = explode_help(t[0], n+1)
    if r:
      if r == t[0]:
        t[0] = 0
      if r[1] >= 0:
        if not isinstance(t[1], list):
          # Regular
          t[1] += r[1]
          r[1] = -1
          return r
        # It must be on the left
        print "look left:", t[1]
        x = t[1]
        while isinstance(x[0], list):
          print x[0]
          x = x[0]
        x[0] += r[1]
        r[1] = -1
    if not r:
      r = explode_help(t[1], n+1)
    if r:
      if r == t[1]:
        t[1] = 0
      if r[0] >= 0 and not isinstance(t[0], list):
        print "set first", r, t
        t[0] += r[0]
        r[0] = -1
      return r
  

def explode(t):
  x = explode_help(t, 0)
  if not x or x == [-1, -1]:
    return x
  print x
  sys.exit()

def splitup(t):
  if not isinstance(t[0], list):
    if t[0] > 9:
      #split
      print "splitting", t[0]
      t[0] = [t[0] / 2, (t[0] + 1) / 2]
      return True
  else:
    if splitup(t[0]):
      return True
  if not isinstance(t[1], list):
    if t[1] > 9:
      #split
      t[1] = [t[1] / 2, (t[1] + 1) / 2]
      return True
  else:
    return splitup(t[1])

l = []
fp = open("test.txt", 'r')
for line in fp:
  line = line.strip()
  line = ast.literal_eval(line)
  if len(l) == 0:
    l = line
  else:
    l = [l, line]

  while True:
    print l
    if explode(l):
      continue
    if not splitup(l):
      break
  print l

