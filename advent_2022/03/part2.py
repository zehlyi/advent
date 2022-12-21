import sys

fp = open("input.txt", 'r')

badges = []
group = []

for line in fp:
    group.append(line.strip())
    if len(group) == 3:
        print group
        for c in group[0]:
            if c in group[1] and c in group[2]:
                badges.append(c)
                break;
        group = []
    

print badges
points = 0
for d in badges:
    if d >= 'a' and d <= 'z':
        points += ord(d) - ord('a') + 1
    else:
        points += ord(d) - ord('A') + 27

print points
