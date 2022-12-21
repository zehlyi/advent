import sys

fp = open("input.txt", 'r')

calories = []
current = 0

for line in fp:
    line = line.strip()
    if line == "":
        calories.append(current)
        current = 0
    else:
        current += int(line)

calories = sorted(calories)
print calories[-3] + calories[-2] + calories[-1]
