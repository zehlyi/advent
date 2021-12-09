with open("in1.txt") as f:
    good = 0
    for line in f:
        arr = sorted(line.strip().split())
        same = True
        for x in range(len(arr) - 1):
            if arr[x] == arr[x+1]:
                same = False
        if same:
            good += 1

print good
