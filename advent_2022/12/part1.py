import sys

paths = {}
g = []
s = [1000, 1000]
e = [1000, 1000]

def insert_path(x, r, c):
    if r == e[0] and c == e[1]:
        print "Found it!", x
        sys.exit()
    if x not in paths:
        paths[x] = []
    paths[x].append([r, c])

def check_paths(rc, s):
    r = rc[0]
    c = rc[1]
    if g[r][c] == 1000:
        return
    if r != 0 and g[r-1][c] - g[r][c] <= 1:
        insert_path(s + 1, r-1, c)
    if r != len(g) - 1 and g[r+1][c] - g[r][c] <= 1:
        insert_path(s + 1, r+1, c)
    if c != 0 and g[r][c-1] - g[r][c] <= 1:
        insert_path(s + 1, r, c-1)
    if c != len(g[0]) - 1 and g[r][c+1] - g[r][c] <= 1:
        insert_path(s + 1, r, c+1)
    g[r][c] = 1000
            
fp = open("input.txt", 'r')
#fp = open("test.txt", 'r')

for line in fp:
    line = line.strip()
    g.append([])
    for c in line:
        if c == 'S':
            s = [len(g) - 1, len(g[-1])]
            c = 'a'
        if c == 'E':
            e = [len(g) - 1, len(g[-1])]
            c = 'z'
        g[-1].append(ord(c))

# Seed
paths[0] = []
paths[0].append([s[0], s[1]])

while True:
    k = sorted(paths.keys())[0]
    to_check = paths[k]
    for p in to_check:    
        check_paths(p, k)
    del paths[k]
    print k
