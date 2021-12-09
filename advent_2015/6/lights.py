f = open("input.txt", 'r')

lights = [[0 for i in range(1000)] for j in range(1000)]

for line in f:
    on = off = toggle = False
    if not line.find("turn on"):
        line = line.strip("turn on ").strip()
        on = True
    if not line.find("turn off"):
        line = line.strip("turn off ").strip()
        off = True
    if not line.find("toggle"):
        line = line.strip("toggle ").strip()
        toggle = True
    start,end = line.split(" through ")
    start_x,start_y = [int(x) for x in start.split(",")]
    end_x,end_y = [int(x) for x in end.split(",")]

    for x in range(start_x, end_x+1):
        for y in range(start_y, end_y+1):
            if on:
                lights[x][y] = 1
            elif off:
                lights[x][y] = 0
            elif toggle:
                if lights[x][y] == 1:
                    lights[x][y] = 0
                else:
                    lights[x][y] = 1

print sum([sum(x) for x in lights]) 
