# With heavy inspiration from reddit...
import sys

program = []
def find(part1):
  solution = [0]* 14
  stack = []

  for i in range(14):
    xadd = int(program[18 * i + 5][2])
    yadd = int(program[18 * i + 15][2])

    if xadd > 0:
      stack.append([yadd, i])
      continue
    s = stack.pop()
    [yadd, yindex] = s[0:2]
    if part1:
      to_add = 9
      while to_add + yadd + xadd > 9:
        to_add -= 1
    else:
      to_add = 1;
      while to_add + yadd + xadd < 1:
        to_add += 1
    solution[yindex] = to_add;
    solution[i] = to_add + yadd + xadd

  return "".join([str(x) for x in solution])


f = open('input.txt', 'r')
for line in f:
  program.append(line.strip().split(' '))

print "Part 1", find(True)
print "Part 2", find(False)
