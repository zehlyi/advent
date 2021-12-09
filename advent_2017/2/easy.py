check = 0
with open("in1.txt") as f:
    for line in f:
        mini = int(line.split()[0])
        maxi = int(line.split()[0])
        for j in line.strip().split():
            i = int(j)
            if i < mini:
                mini = i
            if i > maxi:
                maxi = i
        check += maxi - mini
        print "Added",  maxi - mini, "to check, total now:", check

print check
