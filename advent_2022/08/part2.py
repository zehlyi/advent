import sys

def printarr(a):
    for r in a:
        print r
    print

fp = open("input.txt", 'r')
#fp = open("test.txt", 'r')

t = []

for line in fp:
    line = line.strip()
    t.append([])
    for c in line:
        t[-1].append(c)

scores = []
for r in range(len(t)):
    scores.append([0]* len(t[r]))
for r in range(len(t)):
    for c in range(len(t[r])):
        score = 1
        #check up
        count = 0
        for tree in range(1, c+1):
            count += 1
            if t[r][c - tree] >= t[r][c]:
                break;
        score *= count
        count = 0
        for tree in range(c + 1, len(t[r])):
            count += 1
            if t[r][tree] >= t[r][c]:
                break
        score *= count
        count = 0
        for tree in range(1, r+1):
            count += 1
            if t[r - tree][c] >= t[r][c]:
                break
        score *= count
        count = 0
        for tree in range(r + 1, len(t)):
            count += 1
            if t[tree][c] >= t[r][c]:
                break
        score *= count

        scores[r][c] = score
#printarr(scores)
print max([max(x) for x in scores])
