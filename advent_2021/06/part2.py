import sys

fish = [0] * 9

fp = open("input.txt", 'r')
for line in fp:
  f = line.strip().split(',')
  f = [int(x) for x in f]
  for x in f:
    fish[x] += 1

print fish

for day in range(256):
  next_fish = [0] * 9
  if fish[0] != 0:
    next_fish[6] += fish[0]
    next_fish[8] += fish[0]

  for i in range(1, len(fish)):
    next_fish[i-1] += fish[i]
  print next_fish
  fish = next_fish

count = 0
for f in fish:
  count += f
print("count %d" % count)
