import sys

fp = open("input.txt", 'r')

points = 0

for line in fp:
    first, second = line.strip().split()
    if second == "X":
        if first == "A":
            move = "Z"
        if first == "B":
            move = "X"
        if first == "C":
            move = "Y"
    elif second == "Y":
        points += 3
        if first == "A":
            move = "X"
        if first == "B":
            move = "Y"
        if first == "C":
            move = "Z"
    elif second == "Z":
        points += 6
        if first == "A":
            move = "Y"
        if first == "B":
            move = "Z"
        if first == "C":
            move = "X"
        
    if move == 'X':
        points += 1
    elif move == 'Y':
        points += 2
    elif move == 'Z':
        points += 3

print points
