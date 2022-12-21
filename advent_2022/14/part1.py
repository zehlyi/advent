from __future__ import print_function
import sys


def printscr(s):
    for c in range(len(s[0]), 10):
        for r in range(495, len(s)):
            print(str(s[r][c]), end="")
        print("\n")


fp = open("input.txt", 'r')
#fp = open("test.txt", 'r')

cave = []
for c in range(1000):
    cave.append(['.' for x in range(1000)])

for line in fp:
    line = line.strip().split('->')
    r, c = line[0].strip().split(',')
    oldr = int(r)
    oldc = int(c)
    for l in line[1:]:
        r, c = l.strip().split(',')
        r = int(r)
        c = int(c)
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

grains = 0
while True:
    s_r = 500
    s_c = 0
    while True:
        if s_c > 998:
            print(grains)
            sys.exit()
        if cave[s_r][s_c + 1] == '.':
            s_c += 1
        elif cave[s_r - 1][s_c + 1] == '.':
            s_c += 1
            s_r -= 1
        elif cave[s_r + 1][s_c + 1] == '.':
            s_c += 1
            s_r += 1
        else:
            cave[s_r][s_c] = 'o'
            grains += 1
            break
 
