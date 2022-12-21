import sys

fp = open("input.txt", 'r')
#fp = open("test.txt", 'r')

stacks = []
for i in range(9):
    stacks.append([])
#print stacks

for line in fp:
    line.strip()
    if '[' in line:
        for i in range(len(line)):
            if line[i] >= 'A' and line[i] <= 'Z':
                stacks[i/4].append(line[i])
    elif not "move" in line:
        for s in stacks:
            s.reverse()
        print stacks
    else:
        _, count, _, source, _, dest = line.split()
        count = int(count)
        source = int(source)
        dest = int(dest)

        tmp = stacks[source-1][-count:]
        tmp.reverse()
        stacks[dest-1] += tmp
        stacks[source-1] = stacks[source-1][:-count]
        print
        print stacks

foo = ""
for s in stacks:
    if len(s) > 0:
        foo += s[-1]
print foo

