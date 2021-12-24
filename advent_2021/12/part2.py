import sys

def check(x, links, history, paths):
  if x == "end":
    history.append(x)
    paths.append(history)
    return
  if x not in links:
    return
  for c in links[x]:
    if c == 'start':
       continue
    h = history[0:]
    if c.islower() and c in history:
      if history[0]:
        continue
      else:
        h[0] = True
    h.append(x)
    check(c, links, h, paths)


links = {}
fp = open("input.txt", 'r')
for line in fp:
  a, b = line.strip().split('-')
  if a not in links:
    links[a] = []
  links[a].append(b)
  if b not in links:
    links[b] = []
  links[b].append(a)

#print links
paths = []
history = [False]
check('start', links, history, paths)

#print paths
print len(paths)
