import sys

fp = open("input.txt", 'r')
#fp = open("test.txt", 'r')

tunnels = {}
rates = {}

#Valve AA has flow rate=0; tunnels lead to valves DD, II, BB
for line in fp:
    line = line.strip().split()
    room = line[1]
    rates[room] = int(line[4].strip(';').split('=')[1])
    neighbors = line[9:]
    tunnels[room] = []
    for n in neighbors:
        n = n.strip(',')
        tunnels[room].append(n)

print rates
print tunnels

paths = {}
for t in tunnels:
    paths[t] = {}
paths['AA'][0] = set()

for s in range(30):
    new_paths = {}
    for t in tunnels:
        new_paths[t] = {}
    for r in paths.keys():
        for e in paths[r].keys():
            if rates[r] > 0 and r not in paths[r][e]:
                turned = paths[r][e].copy()
                turned.add(r)
                new_paths[r][e + (29 - s) * rates[r]] = turned

            for n in tunnels[r]:
                turned = paths[r][e].copy()
                new_paths[n][e] = turned
    paths = new_paths
    #print paths

a = []
for r in paths.values():
    if len(r.keys()) != 0:
        a.append(max(sorted(r.keys())))
print max(a)
