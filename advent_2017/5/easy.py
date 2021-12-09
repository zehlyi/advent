t = []

with open("in1.txt") as f:
    for line in f:
        t.append(int(line.strip()))

i = 0
c = 0
while i >= 0 and i < len(t):
    new_i = t[i] + i
    t[i] += 1
    i = new_i
    c += 1

print c
