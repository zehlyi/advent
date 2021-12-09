import sys

fp = open("input", 'r')

level = 0
idx = 0
for line in fp:
    for c in line.strip():
      idx += 1
      if c == '(':
        level += 1
      elif c == ')':
        level -= 1
      if level < 0:
        print idx
        sys.exit(0)

