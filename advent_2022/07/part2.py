import sys

sizes = {}

def recurse(directory, name):
    size = 0
    for d in directory:
        if type(directory[d]) == dict:
            size += recurse(directory[d], d)
        else:
            size += directory[d]
    sizes[size] = name
    return size

fp = open("input.txt", 'r')
#fp = open("test.txt", 'r')

fs = {}
pwd = []

for line in fp:
    line = line.strip().split()
    if line[0] == "$":
        #command
        if line[1] == 'cd':
            if line[2] == "/":
                pwd = []
            elif line[2] == "..":
                pwd = pwd[:-1]
            else:
                pwd.append(line[2])
        #elif line[1] == "ls":
    elif line[0] == "dir":
        ptr = fs
        for d in pwd:
            ptr = ptr[d]
        ptr[line[1]] = {}
    else:
        ptr = fs
        for d in pwd:
            ptr = ptr[d]
        ptr[line[1]] = int(line[0])

print fs
recurse(fs, '/')
print sizes
total = max(sizes)
to_delete = total - 40000000
print to_delete
for s in sorted(sizes.keys()):
    if s >= to_delete:
        print s, sizes[s]
        break
