import sys

well = [['.' for x in range(7)] for y in range(10000)]

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
            if well[bottom + r][left + c] == '#' and p[r][c] == '#':
                return True

fp = open("input.txt", 'r')
#fp = open("test.txt", 'r')

rocks = [['####'], ['.#.','###','.#.'], ['###', '..#','..#'], ['#','#', '#', '#'], ['##', '##']]

#printwell()
for line in fp:
    pattern = line.strip()

#print pattern
print len(pattern)
highest = 0
pat = 0
for i in range(2022):
    piece = rocks[i % len(rocks)]
    height = len(piece)
    bottom = highest + 3
    width = len(piece[0])
    left = 2
    while True:
        push = pattern[pat % len(pattern)]
        pat += 1
        if push == '>':
            if not checkoverlap(piece, bottom, left + 1, height, width):
                left += 1
        elif push == '<':
            if not checkoverlap(piece, bottom, left - 1, height, width):
                left -= 1
        else:
            print "WHAT!!!", push
            sys.exit()
        # fall
        if not checkoverlap(piece, bottom - 1, left, height, width):
            bottom -= 1
        else:
            for r in range(len(piece)):
                for c in range(len(piece[r])):
                    if well[bottom + r][left + c] == '#' and piece[r][c] == '#':
                        print "OH NO"
                        sys.exit()
                    if piece[r][c] == '#':
                        well[bottom + r][left + c] = piece[r][c]
            highest = max(highest, bottom + height)
            break 
print highest
#printwell(highest - 1)
#print highest
#printwell()

