
def step(x, y, xv, yv):
  x += xv
  y += yv
  if xv > 0:
    xv -= 1
  elif xv < 0:
    xv += 1
  yv -= 1
  return [x, y, xv, yv]

def tryout(x, y, xmin, xmax, ymin, ymax, xv, yv):
  while not (x >= xmin and x <= xmax and y >= ymin and y <= ymax):
    if (x < xmin and xv <= 0) or (y < ymin and yv <= 0) or (x > xmax and xv >= 0):
      return 0
    x, y, xv, yv = step(x, y, xv, yv)
  print xv, yv
  return 1
  

xmin = 195
xmax = 238
ymin = -93
ymax = -67

#xmin = 20
#xmax = 30
#ymin = -10
#ymax = -5

x = 0
y = 0

c = 0
for xv in range(1, xmax+1):
  for yv in range(ymin, 1000):
    c += tryout(x, y, xmin, xmax, ymin, ymax, xv, yv)

print c
