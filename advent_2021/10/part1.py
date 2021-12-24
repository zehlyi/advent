import sys

floor = []
fp = open("input.txt", 'r')

o = {'(': ')', '[' : ']', '{' : '}', '<' : '>'}
p = {')' : 3, ']' : 57, '}' : 1197, '>' : 25137}

points = 0
for line in fp:
  line = line.strip()
  stack = []
  for i in range(len(line)):
    c = line[i]
    if c in o.keys():
      stack.append(o[c])
    else:
      if len(stack) == 0 or c != stack[-1]:
        print "found bad in ", line, c
        points += p[c]
        break
      else:
        stack = stack[:-1]
      
print "Points", points
