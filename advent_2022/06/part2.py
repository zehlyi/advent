import sys

fp = open("input.txt", 'r')
#fp = open("test.txt", 'r')


for line in fp:
    line.strip()
    for i in range(14, len(line)):
        sub = line[i-14:i]
        c = 0
        for s in sub:
            if sub.count(s) == 1:
                c += 1
        if c == 14:
            print sub, i
            break
         
