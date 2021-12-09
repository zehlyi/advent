
test = 277678
coords = []
dirs = ["right", "up", "left", "down"]
x = 0
y = 0
d = 0
curr_steps = 0
total_steps = 1
for i in range(0, test):
    coords.append((x, y))
    if dirs[d] == "right":
        x += 1
    elif dirs[d] == "up":
        y += 1
    elif dirs[d] == "left":
        x -= 1
    elif dirs[d] == "down":
        y -=1
    curr_steps += 1
    if curr_steps == total_steps:
        # Need to switch direction
        d = (d + 1) % 4
        if dirs[d] == "left" or dirs[d] == "right":
            total_steps += 1
        curr_steps = 0

tested = coords[-1]
print abs(tested[0]) + abs(tested[1])
