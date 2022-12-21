import sys


fp = open("input.txt", 'r')
#fp = open("test.txt", 'r')


h = [0, 0]
t = [0, 0]
visited = set()
visited.add("0,0")
print visited

for line in fp:
    direct, dist = line.strip().split()
    dist = int(dist)
    for i in range(dist):
        if direct == 'U':
            h[1] += 1
        elif direct == 'D':
            h[1] -= 1
        elif direct == 'L':
            h[0] -=1
        else:
            h[0] += 1
        if h[1] == t[1] and abs(h[0] - t[0]) == 2:
            t[0] = (h[0] + t[0]) / 2
        elif h[0] == t[0] and abs(h[1] - t[1]) == 2:
            t[1] = (h[1] + t[1]) / 2
        elif abs(h[0] - t[0]) + abs(h[1] - t[1]) > 2:
            t[0] += 1 if h[0] > t[0] else -1
            t[1] += 1 if h[1] > t[1] else -1
        visited.add(str(t[0]) + "," + str(t[1]))
        #print "head:", h[0], h[1]
        #print "tail:", t[0], t[1]
print len(visited)
