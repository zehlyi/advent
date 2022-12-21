import sys

sill = 0
well = [['.' for x in range(7)] for y in range(100)]
rocks = [['####'], ['.#.','###','.#.'], ['###', '..#','..#'], ['#','#', '#', '#'], ['##', '##']]
pattern = ""
highest = 0
pat = 0

heights = []

def printwell(start = 0):
    for r in range(len(well) - start):
        if not '#' in well[-r-1]:
            continue
        s = ""
        for c in well[-r-1]:
            s += c
        print s

def checkoverlap(p, bottom, left, height, width):
    if left + width - 1 > 6:
        return True
    if left < 0:
        return True
    if bottom < 0:
        return True 
    for r in range(len(p)):
        for c in range(len(p[r])):
            if well[bottom - sill + r][left + c] == '#' and p[r][c] == '#':
                return True

def simulate(i):
    global well
    global sill
    global highest
    global pat
    piece = rocks[i % len(rocks)]
    height = len(piece)
    bottom = highest + 3
    width = len(piece[0])
    left = 2
    while True:
        push = pattern[pat]
        pat += 1
        pat = pat % len(pattern)
        if pat == 0:
            heights.append(highest)
        if push == '>':
            if not checkoverlap(piece, bottom, left + 1, height, width):
                left += 1
        else:
            if not checkoverlap(piece, bottom, left - 1, height, width):
                left -= 1
        # fall
        if not checkoverlap(piece, bottom - 1, left, height, width):
            bottom -= 1
        else:
            for r in range(len(piece)):
                for c in range(len(piece[r])):
                    if piece[r][c] == '#':
                        well[bottom - sill + r][left + c] = piece[r][c]
            highest = max(highest, bottom + height)
            break
    if highest - sill > 70:
        well = well[30:]
        sill += 30
        for w in range(30):
            well.append(['.' for x in range(7)])

#printwell()
fp = open("input.txt", 'r')
#fp = open("test.txt", 'r')

for line in fp:
    pattern = line.strip()

#print pattern
print "pattern length: ", len(pattern)
#print pattern
i = 0
blocks = 1000000000000 / len(pattern) - 1000
remain = 1000000000000 % len(pattern)  
print "blocks:", blocks
print "remain", remain
# initialize
while i < 1000 * len(pattern):
    simulate(i)
    i += 1
print highest
first = highest

while i < 1001*len(pattern):
    simulate(i)
    i += 1
print highest - first
foo = highest - first

# remainder
while i < 1001*len(pattern) + remain:
    simulate(i)
    i += 1
print highest

print highest + blocks * foo
