import sys

fp = open("input.txt", 'r')
#fp = open("test.txt", 'r')

c = 0
for line in fp:
    line.strip()
    shifts = line.split(',')
    min1, max1 = shifts[0].split('-')
    min2, max2 = shifts[1].split('-')
    min1 = int(min1)
    min2 = int(min2)
    max1 = int(max1)
    max2 = int(max2)
    if min1 <= min2 and max1 >= min2:
        c += 1
    elif min2 <= min1 and max2 >= min1:
        c+= 1
    else:
        print "no", line


print c

