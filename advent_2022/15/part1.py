import sys


fp = open("input.txt", 'r')
#fp = open("test1.txt", 'r')

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

print sensors
print beacons
blocked = []
l = 2000000
#l = 10
for i in range(len(sensors)):
    distance = abs(sensors[i][0] - beacons[i][0]) + abs(sensors[i][1] - beacons[i][1])
    print distance
    if abs(sensors[i][1] - l) <= distance:
        print "row affected"
        width = distance - abs(sensors[i][1] - l)
        blocked.append([sensors[i][0] - width, sensors[i][0] + width])

#print blocked
# [[-882167, 1536445], [-170542, 4358651], [3506595, 3592335]]
blocked = sorted(blocked)
print "blocked", blocked
blocked2 = blocked[:1]
for b in blocked[1:]:
    if b[1] >= blocked2[-1][1]:
        blocked2[-1][1] = b[1]
    elif b[0] <= blocked2[-1][1]:
        blocked2[-1][1] = max(blocked2[-1][1], b[1])
    else:
        blocked2.append(b)

print blocked2
beacons_in_row = set()
for b in beacons:
    if b[1] == l:
        beacons_in_row.add(b[0])
for b in sensors:
    if b[1] == l:
        beacons_in_row.add(b[0])

print beacons_in_row

count = 0
for b in blocked2:
   count += b[1] - b[0] + 1
   for be in beacons_in_row:
        if be <= b[1] and be >= b[0]:
            count -= 1

print count
