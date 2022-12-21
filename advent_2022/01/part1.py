import sys

fp = open("input.txt", 'r')

maximum = 0
current = 0

for line in fp:
    line = line.strip()
    if line == "":
        if current > maximum:
            maximum = current
        current = 0
    else:
        current += int(line)

print maximum
