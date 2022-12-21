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
paths['AAAA'] = {}
paths['AAAA'][0] = set()

for s in range(4, 30):
    print s
    new_paths = {}
    for r in paths.keys():
        r1 = r[:2]
        r2 = r[2:]
        for e in paths[r].keys():
            # Turn 2 valves
            if r1 != r2 and rates[r1] > 0 and r1 not in paths[r][e] and rates[r2] > 0 and r2 not in paths[r][e]:
                turned = paths[r][e].copy()
                turned.add(r1)
                turned.add(r2)
                if r not in new_paths:
                    new_paths[r] = {}
                new_paths[r][e + (29 - s) * rates[r1] + (29 - s) * rates[r2]] = turned
            # Turn 1, move other
            for p in [[r1, r2], [r2, r1]]:
                if rates[p[0]] > 0 and p[0] not in paths[r][e]:
                    turned = paths[r][e].copy()
                    turned.add(p[0])
                    new_rate = e + (29 - s) * rates[p[0]]
                    for n in tunnels[p[1]]:
                        if p[0] < n:
                            path = p[0] + n
                        else:
                            path = n + p[0]
                        if path not in new_paths:
                            new_paths[path] = {}
                        #print r, "turned:", p[0], "moved from", p[1], "to", n, path
                        new_paths[path][new_rate] = turned.copy()
            # Move both
            for p in [[r1, r2], [r2, r1]]:
                for n0 in tunnels[p[0]]:
                    for n1 in tunnels[p[1]]:
                        if n0 < n1:
                            path = n0 + n1
                        else:
                            path = n1 + n0
                        if path not in new_paths:
                            new_paths[path] = {}
                        new_paths[path][e] = paths[r][e].copy()
            
 
    paths = new_paths
    if s < 13:
        continue
    new_paths = {}
    for p in paths.keys():
        sets = {}
        best = {}
        for score in paths[p]:
            hashed = ""
            for s in sorted(paths[p][score]):
                hashed += s
            if hashed not in sets:
                best[hashed] = score
                sets[hashed] = paths[p][score]
            best[hashed] = max(best[hashed], score)
         
        new_paths[p] = {}
        scores = sorted(best.values(), reverse=True)
        limit = scores[min(len(scores) - 1, 100)]
        for hashed in best.keys():
            if best[hashed] >= limit:
                new_paths[p][best[hashed]] = sets[hashed]
    paths = new_paths
    #print s, paths

a = []
for r in paths.values():
    if len(r.keys()) != 0:
        a.append(max(sorted(r.keys())))
print max(a)
