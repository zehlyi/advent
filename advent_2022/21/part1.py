import sys

def scan(monks):
    for m in monks:
        if type(monks[m]) == int:
            continue
        t0 = monks[m][0]
        t1 = monks[m][2]
        if type(t0) != int and type(monks[t0]) == int:
            monks[m][0] = monks[t0]
        if type(t1) != int and type(monks[t1]) == int:
            monks[m][2] = monks[t1]
        if type(monks[m][0]) == int and type(monks[m][2]) == int:
            op = monks[m][1]
            if op == '+':
                monks[m] = monks[m][0] + monks[m][2]
            elif op == '*':
                monks[m] = monks[m][0] * monks[m][2]
            elif op == '-':
                monks[m] = monks[m][0] - monks[m][2]
            elif op == '/':
                monks[m] = monks[m][0] / monks[m][2]
            else:
                print "WHAT"
                sys.exit(0)
        


fp = open("input.txt", 'r')
#fp = open("test.txt", 'r')

monks = {}

for line in fp:
    monkey, exp = line.strip().split(":")
    exp = exp.strip()
    if ' ' in exp:
        exp = exp.split(' ')
        monks[monkey] = exp
    else:
        monks[monkey] = int(exp)

while type(monks['root']) != int:
    scan(monks)   
print monks['root']
