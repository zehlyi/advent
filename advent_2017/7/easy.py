

def connect(subtrees, sub):
    print "connect:", sub
    for s in sub:
        if len(sub[s]) == 0:
            print "check for", s, "in subtrees"
            if s in subtrees:
                print "found", s, "in subtrees"
                # found a match!
                sub[s] = subtrees[s]
                del subtrees[s]
                return True
            return connect(subtrees, sub[s])
        print s, "had subtrees"
    return False


subtrees = {}

with open("test.txt") as f:
    for line in f:
        words = line.strip().split()
        # parent (weight) -> child child child
        t = words[0]
        subtrees[t] = {}
        if len(words) > 2:
            children = words[3:]
            for c in children:
                c = c.strip(",")
                if c in subtrees:
                    # we know its children! Connect up.
                    subtrees[t][c] = subtrees[c]
                    del subtrees[c]
                else:
                    subtrees[t][c] = {}

while len(subtrees) > 1:
    print subtrees
    print subtrees.keys()
    for s in subtrees:
        if len(subtrees[s]) > 0:
            if connect(subtrees, subtrees[s]):
                break
print subtrees
