fp = open('input.txt', 'r')

count = 0
ribbon = 0
for line in fp:
    l,w,h = sorted(int(x) for x in line.strip().split('x'))
    count += 3*l*w + 2*l*h + 2*w*h
    ribbon += 2*(l+w) + l*w*h

print "paper:", count
print "ribbon:", ribbon
    
    
