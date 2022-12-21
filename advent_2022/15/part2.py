import sys


fp = open("input.txt", 'r')
#fp = open("test.txt", 'r')

sensors = []
beacons = []

#Sensor at x=8, y=7: closest beacon is at x=2, y=10
for line in fp:
    line = line.strip().split(':')
    x = line[0].split()[2]
    x = int(x.split('=')[1].strip(','))
    y = line[0].split()[3]
    y = int(y.split('=')[1].strip(':'))
    sensors.append([x, y])
    x = line[1].split()[4]
    x = int(x.split('=')[1].strip(','))
    y = line[1].split()[5]
    y = int(y.split('=')[1])
    beacons.append([x, y])

xymin = 0
xymax = 4000000
for l in range(xymax+1):
    if l % 1000 == 0:
        print l
    blocked = []
    for i in range(len(sensors)):
        distance = abs(sensors[i][0] - beacons[i][0]) + abs(sensors[i][1] - beacons[i][1])
        if abs(sensors[i][1] - l) <= distance:
            width = distance - abs(sensors[i][1] - l)
            blocked.append([sensors[i][0] - width, sensors[i][0] + width])

#print blocked
# [[-882167, 1536445], [-170542, 4358651], [3506595, 3592335]]
# blocked [[-3, 3], [2, 2], [3, 13], [11, 13], [15, 17], [15, 25]]
    beacons_in_row = set()
    for b in beacons:
        if b[1] == l:
            blocked.append([b[0], b[0]])
    for b in sensors:
        if b[1] == l:
            blocked.append([b[0], b[0]])

    blocked = sorted(blocked)
    blocked2 = blocked[:1]
    for b in blocked[1:]:
        if b[0] <= blocked2[-1][1] + 1:
            blocked2[-1][1] = max(blocked2[-1][1], b[1])
        else:
            blocked2.append(b)

    if len(blocked2) > 1:
        print l, blocked2
        sys.exit(0)
