from __future__ import print_function
import sys


def printscr(s):
    for i in range(len(s)):
        if i % 40 == 0:
            print("")
        print(str(s[i]), end="")
    print("\n")


fp = open("input.txt", 'r')
#fp = open("test.txt", 'r')

x = 1
cycles = 0
s = []

for line in fp:
    line = line.strip().split()
    if len(line) == 1:
        # nop
        if cycles % 40 >= x - 1 and cycles  % 40 <= x + 1:
            s.append('#')
        else:
            s.append('.')
        cycles += 1
    else:
        if cycles % 40 >= x - 1 and cycles % 40 <= x + 1:
            s.append('#')
        else:
            s.append('.')
        cycles += 1
        if cycles % 40 >= x - 1 and cycles % 40 <= x + 1:
            s.append('#')
        else:
            s.append('.')
        cycles += 1
        x += int(line[1])
    print("%d, %d" % (cycles, x))
#    if cycles < 5:
#        print(cycles)
#        printscr(s)

print(cycles)
print(x)
printscr(s)
