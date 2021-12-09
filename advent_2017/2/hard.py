check = 0
with open("in1.txt") as f:
    for line in f:
        found = False
        for i in line.strip().split():
            if not found:
                for j in line.strip().split():
                    if not found and i != j:
                        div = float(i) / float(j)
                        if div == int(div):
                            check += int(div)
                            found = True
    
print check
