import sys

class Volume:
  xmin = 0
  xmax = 0
  ymin = 0
  ymax = 0
  zmin = 0
  zmax = 0
  on = False

  def __init__(self, xmin, xmax, ymin, ymax, zmin, zmax, on):
    self.xmin = xmin
    self.xmax = xmax
    self.ymin = ymin
    self.ymax = ymax
    self.zmin = zmin
    self.zmax = zmax
    self.on = on

  def size(self):
    return (self.xmax - self.xmin + 1) * (self.ymax - self.ymin + 1) * (self.zmax - self.zmin + 1)

  def intersect(self, other):
    ixmin = max(self.xmin, other.xmin)
    ixmax = min(self.xmax, other.xmax)
    iymin = max(self.ymin, other.ymin)
    iymax = min(self.ymax, other.ymax)
    izmin = max(self.zmin, other.zmin)
    izmax = min(self.zmax, other.zmax)

    # If any dimension is negative, we didn't really intersect.
    if ixmin > ixmax or iymin > iymax or izmin > izmax:
      return False
    return Volume(ixmin, ixmax, iymin, iymax, izmin, izmax, self.on)

  def subtract(self, other):
    tmp = self.intersect(other)
    if not tmp:
      return []
    vols = []
    if tmp.xmin > self.xmin:
      vols.append(Volume(self.xmin, tmp.xmin-1, self.ymin, self.ymax, self.zmin, self.zmax, on=self.on))
    if self.xmax > tmp.xmax:
      vols.append(Volume(tmp.xmax+1, self.xmax, self.ymin, self.ymax, self.zmin, self.zmax, on=self.on))
    if tmp.ymin > self.ymin:
      vols.append(Volume(tmp.xmin, tmp.xmax, self.ymin, tmp.ymin-1, self.zmin, self.zmax, on=self.on))
    if self.ymax > tmp.ymax:
      vols.append(Volume(tmp.xmin, tmp.xmax, tmp.ymax+1, self.ymax, self.zmin, self.zmax, on=self.on))
    if tmp.zmin > self.zmin:
      vols.append(Volume(tmp.xmin, tmp.xmax, tmp.ymin, tmp.ymax, self.zmin, tmp.zmin-1, on=self.on))
    if self.zmax > tmp.zmax:
      vols.append(Volume(tmp.xmin, tmp.xmax, tmp.ymin, tmp.ymax, tmp.zmax+1, self.zmax, on=self.on))
    return vols

blocks = set()

total = 0
fp = open("input.txt", 'r')
for line in fp:
  toggle, dims = line.strip().split(' ')
  xr, yr, zr = dims.split(',')
  xmin, xmax = xr[2:].split('..')
  xmin = int(xmin)
  xmax = int(xmax)
  ymin, ymax = yr[2:].split('..')
  ymin = int(ymin)
  ymax = int(ymax)
  zmin, zmax = zr[2:].split('..')
  zmin = int(zmin)
  zmax = int(zmax)
  toggle = True if toggle == "on" else False

  v = Volume(xmin, xmax, ymin, ymax, zmin, zmax, toggle)
  for other in list(blocks):
    if v.intersect(other):
      blocks.update(other.subtract(v))
      blocks.remove(other)
  blocks.add(v)
  #print [[v.xmin, v.xmax, v.ymin, v.ymax, v.zmin, v.zmax, v.on] for v in list(blocks)]
  print sum(x.size() for x in blocks if x.on)
print sum(x.size() for x in blocks if x.on)
  
