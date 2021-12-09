import string

file = open("input.txt", 'r')

evil = ["ab", "cd", "pq", "xy"]
count = 0

for s in file:
    vowel = 0
    double = False
    if string.find(s, evil[0]) + string.find(s, evil[1]) + string.find(s, evil[2]) + string.find(s, evil[3]) > -4:
        print ("Boo", s) 
        continue
    for l in range(len(s)-1):
        if s[l] in "aeiou":
            vowel += 1
        if s[l] == s[l+1]:
            double = True
    if vowel >= 3 and double:
        count += 1
        print s.strip()

print "count: ", count
