import sys

fp = open("input.txt", 'r')

h = 0
d = 0
for line in fp:
  direction, magnitude = line.strip().split()
  magnitude = int(magnitude)
  if direction == "up":
    d = d - magnitude
  elif direction == "down":
    d = d + magnitude
  elif direction == "forward":
    h = h + magnitude
  elif direction == "back":
    h = h - magnitude

print("h: %d; d: %d; product: %d" % (h, d, h*d))
