test = 277678

def get_diagonals(grid, my_x, my_y):
    tot = 0
    for x in [my_x-1, my_x, my_x+1]:
        if x not in grid:
            continue
        for y in [my_y-1, my_y, my_y+1]:
            if y in grid[x]:
                tot += grid[x][y]

    return tot

coords = []
dirs = ["right", "up", "left", "down"]
x = 0
y = 0
d = 0
grid = {}
curr_steps = 0
total_steps = 1
last = 1
while last < test:
    if not x in grid:
        grid[x] = {}
    grid[x][y] = get_diagonals(grid, x, y)
    if grid[x][y] == 0:
        grid[x][y] = 1
    last = grid[x][y]
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

print last
