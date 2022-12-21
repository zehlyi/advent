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

def compare2(a, b):
    r = compare(a, b)
    if r == True:
        return -1
    if r == False:
        return 1
    return 0
            

fp = open("input.txt", 'r')
#fp = open("test.txt", 'r')

packets = []
packets.append([[2]])
packets.append([[6]])

for line in fp:
    line = line.strip()
    if len(line) > 0:
        packets.append(ast.literal_eval(line))

k = 1
packets = sorted(packets, compare2)
for p in range(len(packets)):
    if packets[p] == [[2]]:
        k *= p + 1
    elif packets[p] == [[6]]:
        k *= p + 1
print k
