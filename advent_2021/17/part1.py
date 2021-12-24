
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
  top_y = 0
  while not (x >= xmin and x <= xmax and y >= ymin and y <= ymax):
    if (x < xmin and xv <= 0) or (y < ymin and yv <= 0) or (x > xmax and xv >= 0):
      return -1
    x, y, xv, yv = step(x, y, xv, yv)
    top_y = y if y > top_y else top_y
  return top_y
  

xmin = 195
xmax = 238
ymin = -93
ymax = -67

x = 0
y = 0

best = 0
for xv in range(1, xmax):
  for yv in range(ymin, 1000):
    t =  tryout(x, y, xmin, xmax, ymin, ymax, xv, yv)
    if t > best:
      best = t

print best
