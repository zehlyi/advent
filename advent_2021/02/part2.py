import sys

fp = open("input.txt", 'r')

h = 0
d = 0
a = 0
for line in fp:
  direction, magnitude = line.strip().split()
  magnitude = int(magnitude)
  if direction == "up":
    a -= magnitude
  elif direction == "down":
    a += magnitude
  elif direction == "forward":
    h += magnitude
    d += a * magnitude 

print("h: %d; d: %d; product: %d" % (h, d, h*d))
