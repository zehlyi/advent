from __future__ import print_function
import sys


def printscr(s):
    for c in range(15):
        for r in range(495, 505):
            print(str(s[r][c]), end="")
        print("\n")


fp = open("input.txt", 'r')
#fp = open("test.txt", 'r')

cave = []
for c in range(1000):
    cave.append(['.' for x in range(1000)])

maxc = 0
for line in fp:
    line = line.strip().split('->')
    r, c = line[0].strip().split(',')
    oldr = int(r)
    oldc = int(c)
    if oldc > maxc:
        maxc = oldc
    for l in line[1:]:
        r, c = l.strip().split(',')
        r = int(r)
        c = int(c)
        if c > maxc:
            maxc = c
        for f in range(r, oldr + 1):
            cave[f][c] = '#'
        for f in range(oldr, r + 1):
            cave[f][c] = '#'
        for f in range(c, oldc + 1):
            cave[r][f] = '#'
        for f in range(oldc, c + 1):
            cave[r][f] = '#'
        oldr = r
        oldc = c
cave[500][0] = '+'
for r in range(len(cave)):
    cave[r] = cave[r][:maxc + 3]
    cave[r][-1] = '#'

grains = 1
while True:
    s_r = 500
    s_c = 0
    while True:
        if cave[s_r][s_c + 1] == '.':
            s_c += 1
        elif cave[s_r - 1][s_c + 1] == '.':
            s_c += 1
            s_r -= 1
        elif cave[s_r + 1][s_c + 1] == '.':
            s_c += 1
            s_r += 1
        elif s_r == 500 and s_c == 0:
            print(grains)
            sys.exit(0)
        else:
            cave[s_r][s_c] = 'o'
            grains += 1
            break
 
