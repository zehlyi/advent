import sys

def CheckWinner(cand):
  for r in cand:
    if max(r) == -1:
      return True
  # Columns
  for col in range(5):
    total = 0
    for row in range(5):
      total += cand[row][col]
    if total == -5:
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
  to_delete = []
  for board in boards:
    MarkBoard(board, move)
    #print board
    if CheckWinner(board):
      print("a board won")
      if len(boards) == 1:
        print("We're done!")
        points = CountPoints(board)
        print("points: %d, move: %d, total: %d" % (points, move, points*move))
        sys.exit()
      to_delete.append(board)
  # Delete any boards that already won
  for board in to_delete:
    boards.remove(board)
