import sys
import ast

def compare(a, b):
    if type(a) == int and type(b) == int:
        if a < b:
            return True
        if a > b:
            return False
        return None
    if type(a) == int:
        a = [a]
    elif type(b) == int:
        b = [b]
    if type(a) == list and type(b) == list:
        for i in range(min(len(a), len(b))):
            ret = compare(a[i], b[i])
            if ret != None:
                return ret
        if len(a) < len(b):
            return True
        if len(a) > len(b):
            return False
        return None
    else:
        print "What??"
            

fp = open("input.txt", 'r')
#fp = open("test.txt", 'r')

p1 = []
p2 = []
i = -1
idx = 1
right = []

for line in fp:
    i += 1
    if i % 3 == 2:
        continue
    line = line.strip()
    if i % 3 == 0:
        p1 = ast.literal_eval(line)
        continue
    p2 = ast.literal_eval(line)
    
    if compare(p1, p2):
        right.append(idx)
    idx += 1

print sum(right)
