import sys


fp = open("input.txt", 'r')
#fp = open("test.txt", 'r')

x = 1
cycles = 0
signal = []

for line in fp:
    line = line.strip().split()
    if len(line) == 1:
        # nop
        cycles += 1
        if cycles == 20 or (cycles - 20) % 40 == 0:
        #    print "a", cycles, x
            signal.append(x * cycles)
    else:
        cycles += 1
        if cycles == 20 or (cycles - 20) % 40 == 0:
        #    print "b", cycles, x
            signal.append(x * cycles)
        cycles += 1
        if cycles == 20 or (cycles - 20) % 40 == 0:
        #    print "c", cycles, x
            signal.append(x * cycles)
        x += int(line[1])

print cycles
print x
print signal
print sum(signal)
