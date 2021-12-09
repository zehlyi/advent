
f = open('input1.txt', 'r')
total = 0
for line in f:
  total += int(line.strip())

print total
