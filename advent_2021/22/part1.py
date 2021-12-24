import sys

def togglebit(a, x, y, z, toggle):
  if x not in a:
    a[x] = {}
  if y not in a[x]:
    a[x][y] = {}
  if z not in a[x][y]:
    a[x][y][z] = 0
  temp = a[x][y][z]
  a[x][y][z] = toggle
  return toggle - temp

ones = {}
total = 0

maximum = 50
minimum = -50

fp = open("input.txt", 'r')
for line in fp:
  toggle, dims = line.strip().split(' ')
  xr, yr, zr = dims.split(',')
  xmin, xmax = xr[2:].split('..')
  xmin = int(xmin)
  xmax = int(xmax)
  if xmin > maximum or xmax > maximum:
    continue
  if xmin < minimum or xmax < minimum:
    continue
  ymin, ymax = yr[2:].split('..')
  ymin = int(ymin)
  ymax = int(ymax)
  if ymin > maximum or ymax > maximum:
    continue
  if ymin < minimum or ymax < minimum:
    continue
  zmin, zmax = zr[2:].split('..')
  zmin = int(zmin)
  zmax = int(zmax)
  if zmin > maximum or zmax > maximum:
    continue
  if zmin < minimum or zmax < minimum:
    continue

  toggle = 1 if toggle == "on" else 0
  for x in range(xmin, xmax + 1):
    for y in range(ymin, ymax + 1):
      for z in range(zmin, zmax + 1):
        total += togglebit(ones, x, y, z, toggle)
  print total
