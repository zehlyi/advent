with open("in1.txt") as f:
    good = 0
    for line in f:
        words = line.strip().split()
        sorted_words = ["".join(sorted(x)) for x in words]
        arr = sorted(sorted_words)
        same = True
        for x in range(len(arr) - 1):
            if arr[x] == arr[x+1]:
                same = False
        if same:
            good += 1

print good
