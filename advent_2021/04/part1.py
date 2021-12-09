import sys

def CheckWinner(cand):
  for r in cand:
    if max(r) == -1:
      return True
  # Columns
  for i in range(5):
    total = 0
    for j in range(5):
      total += cand[j][i]
    if prod == -5:
      return True

def MarkBoard(board, number):
  for r in range(5):
    for c in range(5):
       if board[r][c] == number:
         board[r][c] = -1

def CountPoints(board):
  total = 0
  for r in range(5):
    for c in range(5):
      if board[r][c] != -1:
        total += board[r][c]
  return total
        

fp = open("input.txt", 'r')

moves = []
boards = []
b = []

for line in fp:
  if len(moves) == 0:
    moves = line.strip().split(',')
    moves = [int(x) for x in moves]
    #print moves
    continue

  if line.strip() == "":
    continue

  # This must be a board
  spots = line.strip().split()
  spots = [int(x) for x in spots]
  b.append(spots)
  if len(b) == 5:
    boards.append(b)
    b = []

print boards

for move in moves:
  print("Move is: %d" % move)
  for board in boards:
    MarkBoard(board, move)
    #print board
    if CheckWinner(board):
      print("We won!")
      points = CountPoints(board)
      print("points: %d, move: %d, total: %d" % (points, move, points*move))
      sys.exit()
