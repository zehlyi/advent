import sys

b = [4, 1]

p = [0, 0]

d = 0
rolls = 0

while p[0] < 1000 and p[1] < 1000:
  for x in range(2):
    dice = 0
    for i in range(3):
      rolls += 1
      d = (d % 100) + 1
      dice += d
    b[x] = ((b[x] + dice - 1) % 10) + 1
    p[x] += b[x]
    if p[x] >= 1000:
      break

print "points", p
print "board", b
print "rolls", rolls
print "answer", min(p) * rolls
