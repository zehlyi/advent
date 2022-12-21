import sys

fp = open("input.txt", 'r')

points = 0

for line in fp:
    first, second = line.strip().split()
    if second == 'X':
        points += 1
    elif second == 'Y':
        points += 2
    elif second == 'Z':
        points += 3
    if first == "A" and second == "X" or first == "B" and second == "Y" or first == "C" and second == "Z":
        points += 3
    if first == "A" and second == "Y" or first == "B" and second == "Z" or first == "C" and second =="X":
        points += 6
    

print points
