
def get_max_index(a):
    v = a[0]
    ind = 0
    for i in range(1, len(a)):
        if a[i] > v:
            v = a[i]
            ind = i
    return ind

def check_helper(boards, curr):
    if len(curr) == 1:
        if curr[0] not in boards:
            boards[curr[0]] = 1
            return False
        else:
            return True
    if curr[0] not in boards:
        boards[curr[0]] = {}
    return check_helper(boards[curr[0]], curr[1:])

all_boards = {}
def add_and_check_board(a):
    return check_helper(all_boards, a)


arr = []
with open("in1.txt") as f:
    for line in f:
        arr = line.strip().split()
        break
for i in range(len(arr)):
    arr[i] = int(arr[i])
count = 0

while not add_and_check_board(arr):
    count += 1
    max_ind = get_max_index(arr)
    i = max_ind + 1
    outstanding = arr[max_ind]
    arr[max_ind] = 0
    while outstanding > 0:
        i = i % len(arr)
        arr[i] += 1
        outstanding -= 1
        i += 1
    print arr
print count
