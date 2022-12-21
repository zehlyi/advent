import sys

#Monkey 0:
#  Starting items: 79, 98
#  Operation: new = old * 19
#  Test: divisible by 23
#    If true: throw to monkey 2
#    If false: throw to monkey 3

fp = open("input.txt", 'r')
#fp = open("test.txt", 'r')

items = []
operation = []
divisor = []
true = []
false = []

idx = -1
for line in fp:
    line = line.strip().split()
    print line
    if len(line) == 0:
        continue
    if line[0] == "Monkey":
        idx = int(line[1][:-1])
        items.append([])
    elif line[0] == "Starting":
        for i in line[2:]:
            items[idx].append(int(i.strip(",")))
    elif line[0] == "Operation:":
        operation.append(' '.join(line[3:]))
    elif line[0] == "Test:":
        divisor.append(int(line[3]))
    elif line[1] == "true:":
        true.append(int(line[5]))
    elif line[1] == "false:":
        false.append(int(line[5]))
        

print items
print operation
print divisor
print true
print false

count = []
for m in range(len(items)):
    count.append(0)

for c in range(20):
    for m in range(len(items)):
        while len(items[m]) > 0:
            i = items[m].pop(0)
            f = lambda old : eval(operation[m])
            i = f(i)
            count[m] += 1
            i = i / 3
            if i % divisor[m] == 0:
                items[true[m]].append(i)
            else:
                items[false[m]].append(i)

print items
print count
count = sorted(count)
print count[-1]*count[-2]
