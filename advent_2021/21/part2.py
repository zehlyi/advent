import sys

def dict_add(a, points1, points2, count):
  if points1 not in a:
    a[points1] = {}
  if points2 not in a[points1]:
    a[points1][points2] = 0
  a[points1][points2] += count

# pos1, pos2, pts1, pts2, count
b = []
for j in range(11):
  b.append([])
  for i in range(11):
    b[j].append({})
# Starting positions go in here.
dict_add(b[4][1], 0, 0, 1)
d = [0] * 10

for i in range(1, 4):
  for j in range(1, 4):
    for k in range(1, 4):
      d[i + j + k] += 1

wins = [0, 0]
did_something = True

player = 0
while did_something:
  did_something = False
  new_b = []
  for j in range(11):
    new_b.append([])
    for i in range(11):
      new_b[j].append({})

  for pos in range(len(b)):
    for i in range(3, 10):
      new_pos = ((pos + i - 1) % 10) + 1
      for other_pos in range(len(b[pos])):
        for pts in b[pos][other_pos].keys():
          did_something = True
          new_pts = new_pos + pts
          if new_pts >= 21:
            wins[player] += sum(b[pos][other_pos][pts].values()) * d[i]
          else:
            for opts in b[pos][other_pos][pts].keys():
              dict_add(new_b[other_pos][new_pos], opts, new_pts, b[pos][other_pos][pts][opts] * d[i])
  b = new_b
  player = (player + 1) % 2

print wins
