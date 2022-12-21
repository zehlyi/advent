import sys

def printit(a):
    f = []
    for i in range(20):
        f.append(["."]*20)
    for i in range(len(a)):
        x = a[i][0]
        y = a[i][1]
        f[10+(-1*y)][10+x] = i

    for l in f:
        for c in l:
            print c,
        print


fp = open("input.txt", 'r')
#fp = open("test2.txt", 'r')


r = []
for i in range(10):
    r.append([0, 0])
visited = set()
visited.add("0,0")
print visited

for line in fp:
    direct, dist = line.strip().split()
    dist = int(dist)
    for i in range(dist):
        print direct, i
        if direct == 'U':
            r[0][1] += 1
        elif direct == 'D':
            r[0][1] -= 1
        elif direct == 'L':
            r[0][0] -=1
        else:
            r[0][0] += 1
        for j in range(1, len(r)):
            if r[j-1][1] == r[j][1] and abs(r[j-1][0] - r[j][0]) == 2:
                r[j][0] = (r[j-1][0] + r[j][0]) / 2
            elif r[j-1][0] == r[j][0] and abs(r[j-1][1] - r[j][1]) == 2:
                r[j][1] = (r[j-1][1] + r[j][1]) / 2
            elif abs(r[j-1][0] - r[j][0]) + abs(r[j-1][1] - r[j][1]) > 2:
                if direct == "L" and i == 3:
                    print "what", j
                r[j][0] += 1 if r[j-1][0] > r[j][0] else -1
                r[j][1] += 1 if r[j-1][1] > r[j][1] else -1
        visited.add(str(r[-1][0]) + "," + str(r[-1][1]))
        #print "head:", h[0], h[1]
        #print "tail:", t[0], t[1]
print len(visited)
