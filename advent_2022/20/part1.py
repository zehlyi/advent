import sys

fp = open("input.txt", 'r')
#fp = open("test.txt", 'r')

a = []
i = 0
for line in fp:
    line = line.strip()
    a.append([i, int(line)])
    i += 1
#print a

j = 0
for i in range(len(a)):
    while a[j][0] != i:
        j += 1
    #print j, len(a)
    move = a[j][1]
    if move == 0:
        continue
    new_j = (j + a[j][1]) % (len(a)-1)
    if j < new_j:
        a = a[:j] + a[j+1:]
        a = a[:new_j] + [[i, move]] + a[new_j:]
    else:
        a = a[:new_j] + [[i, move]] + a[new_j:j] + a[j+1:]

for i in range(len(a)):
    if a[i][1] == 0:
        break

print a[(i + 1000) % len(a)][1] + a[(i + 2000) % len(a)][1] + a[(i + 3000) % len(a)][1]

