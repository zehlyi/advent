import sys

def scan(monks):
    for m in monks:
        if type(monks[m]) == int:
            continue
        if type(monks[m]) == str:
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

def unscan(monks):
    for m in monks:
        if type(monks[m]) == int:
            continue
        if type(monks[m]) == str:
            continue
        if len(monks[m]) == 3:
            if monks[m][1] == '=':
                if type(monks[m][0]) == int:
                    monks[monks[m][2]] += ['=', monks[m][0]]
                    monks[m] = "-"
                elif type(monks[m][2]) == int:
                    monks[monks[m][0]] += ['=', monks[m][2]]
                    monks[m] = "-"
        elif len(monks[m]) > 3:
            a, op, b, eq, c = monks[m]
            if type(a) == str and type(b) == int:
                rep = a
                if op == '+':
                    monks[rep] += ['=',  c - b]
                elif op == '-':
                    monks[rep] += ['=', c + b]
                elif op == '*':
                    monks[rep] += ['=', c / b]
                elif op == '/':
                    monks[rep] += ['=', c * b]
                else:
                    print "What"
                    sys.exit(0)
                monks[m] = "-"
            elif type(a) == int and type(b) == str:
                rep = b
                if op == '+':
                    monks[rep] += ['=',  c - a]
                elif op == '-':
                    monks[rep] += ['=', a - c]
                elif op == '*':
                    monks[rep] += ['=', c / a]
                elif op == '/':
                    monks[rep] += ['=', c * a]
                else:
                    print "What"
                    sys.exit(0)
                monks[m] = "-"
    monks2 = {}
    for m in monks:
        if type(monks[m]) != str or monks[m] != '-':
            monks2[m] = monks[m]
    monks = monks2
        

                

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
monks['humn'] = '?'
monks['root'][1] = '='

for i in range(1000):
    scan(monks)

monks2 = {}
for m in monks:
    if type(monks[m]) != int:
        monks2[m] = monks[m]
monks = monks2
monks['humn'] = ['?']
monks['?'] = []
while len(monks['?']) == 0:
    #print "unscan"
    unscan(monks)
    #print monks

print monks['?'][1]
