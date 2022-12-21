import sys

def printarr(a):
    for r in a:
        print r
    print

fp = open("input.txt", 'r')
#fp = open("test.txt", 'r')

t = []

for line in fp:
    line = line.strip()
    t.append([])
    for c in line:
        t[-1].append(c)

#print t
visible = []
for r in range(len(t)):
    visible.append([False]* len(t[r]))

for r in range(len(t)):
    maxa = -1
    maxb = -1
    for c in range(len(t[r])):
        if t[r][c] > maxa:
            maxa = t[r][c]
            visible[r][c] = True
        if t[r][-c-1] > maxb:
            maxb = t[r][-c-1]
            visible[r][-c-1] = True
#printarr(visible)
for c in range(len(t[0])):
    maxa = -1
    maxb = -1
    for r in range(len(t)):
        if t[r][c] > maxa:
            maxa = t[r][c]
            visible[r][c] = True
        if t[-r-1][c] > maxb:
            maxb = t[-r-1][c]
            visible[-r-1][c] = True
#printarr(visible)

count = 0
for r in visible:
    count += sum(r)

print count
