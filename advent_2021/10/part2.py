import sys

floor = []
fp = open("input.txt", 'r')

o = {'(': ')', '[' : ']', '{' : '}', '<' : '>'}
p = {')' : 1, ']' : 2, '}' : 3, '>' : 4}

points = []
for line in fp:
  line = line.strip()
  stack = []
  bad = False
  for i in range(len(line)):
    c = line[i]
    if c in o.keys():
      stack.append(o[c])
    else:
      if len(stack) == 0 or c != stack[-1]:
        #print "found bad in ", line, c
        bad = True
        break
      else:
        stack = stack[:-1]

  if bad or len(stack) == 0:
    continue

  pts = 0
  for i in reversed(stack):
    pts = pts * 5 + p[i]
  #print "Incomplete conclusion:", "".join(stack), "worth", pts
  points.append(pts)

points = sorted(points) 
print "Points"
print "Median", points[len(points) / 2]
