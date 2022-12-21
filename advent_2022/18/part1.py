import sys



fp = open("input.txt", 'r')
#fp = open("test.txt", 'r')

def dictadd(a, b, c, d):
    if a not in d:
        d[a] = {}
    if b not in d[a]:
        d[a][b] = []
    d[a][b].append(c)

def edgecheck(a, b, c, d):
    if a not in d or b not in d[a]:
        return 0
    ret = 0
    if c - 1 in d[a][b]:
        ret += 1
    if c + 1 in d[a][b]:
        ret += 1
    return 2*ret

xyz = {}
xzy = {}
yzx = {}

covered = 0
total = 0
for line in fp:
    line = line.strip().split(',')
    total += 6
    [x, y, z] = [int(i) for i in line]
    dictadd(x, y, z, xyz)
    dictadd(x, z, y, xzy)
    dictadd(y, z, x, yzx)
    covered += edgecheck(x, y, z, xyz)
    covered += edgecheck(x, z, y, xzy)
    covered += edgecheck(y, z, x, yzx)

print total - covered
