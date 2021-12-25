import sys

paper = []
insts = []

fp = open("input.txt", 'r')
for line in fp:
  if len(line.strip()) == 0:
    continue
  if not ',' in line:
    insts.append(line.strip().split(' ')[-1])
    continue
  x,y = line.strip().split(',')
  x = int(x)
  y = int(y)
  if y >= len(paper):
    for i in range(len(paper) - 1, y+1):
      paper.append(1311 * [False])
  paper[y][x] = True

#for y in range(len(paper)):
#  for x in range(len(paper[y])):
#    print '#' if paper[y][x] else '.',
#  print

print insts

for i in insts:
  d,m = i.split(" ")[-1].split("=")
  m = int(m)
  if d == 'y':
    # horizontal
    for y in range(m):
      for x in range(len(paper[y])):
        paper[y][x] = paper[y][x] or paper[2*m-y][x]
    paper = paper[0:m]
  else:
    # vertical
    for y in range(len(paper)):
      for x in range(m):
        paper[y][x] = paper[y][x] or paper[y][2*m-x]
      paper[y] = paper[y][0:m]

for y in range(len(paper)):
  for x in range(len(paper[y])):
    print '#' if paper[y][x] else ' ',
  print

