import sys

STOCK = 1

ORE = 0
CLAY = 1
OBSIDIAN = 2
GEODE = 3
steps = 32

def calculate(costs):
    worlds = [[[1, 0, 0, 0], [0, 0, 0, 0], False]]
    for i in range(steps):
        new_worlds = []
        geode_floor = 0
        for w in range(len(worlds)):
            robots, ores, last_skipped = worlds[w]
            # print robots, ores
            # mine
            new_ores = []
            for r in range(4):
                new_ores.append(ores[r] + robots[r])
            if new_ores[GEODE] + (robots[GEODE] + steps - i) * (steps - i) < geode_floor:
                continue
            # build robots
            if ores[ORE] >= costs[GEODE][0] and ores[OBSIDIAN] >= costs[GEODE][1]:
                if (not last_skipped) or (ores[ORE] - robots[ORE] < costs[GEODE][0] or ores[OBSIDIAN] - robots[OBSIDIAN] < costs[GEODE][1]):
                    new_bots = [r for r in robots]
                    newer_ores = [o for o in new_ores]
                    new_bots[GEODE] += 1
                    newer_ores[ORE] -= costs[GEODE][0]
                    newer_ores[OBSIDIAN] -= costs[GEODE][1]
                    geode_floor = max(geode_floor, ores[GEODE] + (steps - i) * robots[GEODE])
                    new_worlds.append([new_bots, newer_ores, False])
            if ores[ORE] >= costs[OBSIDIAN][0] and ores[CLAY] >= costs[OBSIDIAN][1]:
                if (not last_skipped) or (ores[ORE] - robots[ORE] < costs[OBSIDIAN][0] or ores[CLAY] - robots[CLAY] < costs[OBSIDIAN][1]):
                    new_bots = [r for r in robots]
                    newer_ores = [o for o in new_ores]
                    new_bots[OBSIDIAN] += 1
                    newer_ores[ORE] -= costs[OBSIDIAN][0]
                    newer_ores[CLAY] -= costs[OBSIDIAN][1]
                    new_worlds.append([new_bots, newer_ores, False])
            if ores[ORE] >= costs[CLAY] and robots[CLAY] < costs[OBSIDIAN][1]:
                if not last_skipped or ores[ORE] - robots[ORE] < costs[CLAY]:
                    new_bots = [r for r in robots]
                    newer_ores = [o for o in new_ores]
                    new_bots[CLAY] += 1
                    newer_ores[ORE] -= costs[CLAY]
                    new_worlds.append([new_bots, newer_ores, False])
            if ores[ORE] >= costs[ORE] and robots[ORE] < [max(costs[GEODE][0], costs[OBSIDIAN][0], costs[CLAY])]:
                if not last_skipped or ores[ORE] - robots[ORE] < costs[ORE]:
                    new_bots = [r for r in robots]
                    newer_ores = [o for o in new_ores]
                    new_bots[ORE] += 1
                    newer_ores[ORE] -= costs[ORE]
                    new_worlds.append([new_bots, newer_ores, False])
            new_bots = [r for r in robots]
            newer_ores = [o for o in new_ores]
            new_worlds.append([new_bots, newer_ores, True])
        worlds = []
        robots = [0, 0, 0, 0]
        best = [0, 0, 0, 0]
        for w in sorted(new_worlds, reverse=True):
            r, o, skipped = w
            if r == robots:
                good = False
                for x in range(4):
                    if o[x] > best[x]:
                        good = True
                        break
                if not good:
                    continue
            robots = r
            best = [o[x] for x in range(len(o))]
            worlds.append(w)

        print i, len(worlds), "worlds to check after pruning"
    best_geodes = 0
    for w in worlds:
        best_geodes = max(best_geodes, w[STOCK][GEODE])
    return best_geodes

fp = open("input.txt", 'r')
#fp = open("test.txt", 'r')

count = []
i = 0
for line in fp:
    line = line.strip().split()
    ore = int(line[6])
    clay = int(line[12])
    obsidian = [int(line[18]), int(line[21])]
    geode = [int(line[27]), int(line[30])]

#    print ore, clay, obsidian, geode
    count.append(calculate([ore, clay, obsidian, geode]))
    if i == 2:
        break
    i += 1

print count
print count[0] * count[1] * count[2]
