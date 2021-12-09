import string

file = open("input.txt", 'r')

count = 0

for s in file:
    double = False
    between = False
    for l in range(len(s)-2):
        if s[l] == s[l+2]:
            between = True
        if string.find(s[l+2:], s[l:l+2]) >= 0:
            double = True
    if between and double:
        count += 1

print "count: ", count
