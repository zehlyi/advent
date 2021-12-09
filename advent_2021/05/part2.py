import sys

fp = open("input.txt", 'r')

s = 1000
a = s * s * [0]
print a

for line in fp:
  [p1, p2] = line.strip().split(' -> ')
  [x1, y1] = p1.split(',')
  [x2, y2] = p2.split(',')

  x1 = int(x1)
  x2 = int(x2)
  y1 = int(y1)
  y2 = int(y2)

  print ("%d %d %d %d" % (x1, y1, x2, y2))
  if x1 != x2 and y1 != y2:
    if x1 < x2 and y1 < y2 or x2 < x1 and y2 < y1:
      # down to the right
      x = min(x1, x2)
      y = min(y1, y2)
      while y <= max(y1, y2):
        a[y * s + x] += 1
        y += 1
        x += 1
    else:
      # down to the left
      x = max(x1, x2)
      y = min(y1, y2)
      while y <= max(y1, y2):
        a[y * s + x] += 1
        y += 1
        x -= 1
    continue

  if x1 == x2:
    y = min(y1, y2)
    while y <= max(y1, y2):
      a[y * s + x1] += 1
      y += 1
  else:
    x = min(x1, x2)
    while x <= max(x1, x2):
      a[y1 * s + x] += 1
      x += 1

count = 0
for i in range(s):
  for j in range(s):
    print a[i * s + j],
    if a[i * s + j] > 1:
      count += 1
  print

print count
