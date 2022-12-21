import sys

fp = open("input.txt", 'r')

duplicates = []

for line in fp:
    line.strip()
    pivot = len(line) / 2
    first = line[:pivot]
    second = line[pivot:]

    for i in first:
        if i in second:
            duplicates.append(i)
            break

print duplicates
points = 0
for d in duplicates:
    if d >= 'a' and d <= 'z':
        points += ord(d) - ord('a') + 1
    else:
        points += ord(d) - ord('A') + 27

print points
