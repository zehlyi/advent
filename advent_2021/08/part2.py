import sys

#   000
#  1   2
#   333
#  4   5
#   666

mapping = [[0,1,2,4,5,6], [2,5], [0, 2, 3, 4, 6], [0, 2, 3, 5, 6], [1, 2, 3, 5], [0, 1, 3, 5, 6], [0, 1, 3, 4, 5, 6], [0, 2, 5], [0, 1, 2, 3, 4, 5, 6], [0, 1, 2, 3, 5, 6]]

def do_update(digit, dig_segs, poss_segs):
  print digit, dig_segs, poss_segs
  for s in range(7):
    if s in mapping[digit]:
      # Then the only segs in there should be the ones in dig_segs.
      poss_segs[s] = "".join([x for x in poss_segs[s] if x in dig_segs])
    else:
      # Then the ones in dig_segs can't be there.
      poss_segs[s] = "".join([x for x in poss_segs[s] if x not in dig_segs])
  print "poss_segs",  poss_segs
  
def compare(digit1, digit2, keys, poss_segs):
  for s in range(7):
    if s in mapping[digit1] and s in mapping[digit2]:
      # segment must be in both digits
      poss_segs[s] = "".join([x for x in poss_segs[s] if x in keys[digit1] and x in keys[digit2]]) 
    elif s in mapping[digit1]:
      poss_segs[s] = "".join([x for x in poss_segs[s] if x in keys[digit1] and x not in keys[digit2]]) 
    elif s in mapping[digit2]:
      poss_segs[s] = "".join([x for x in poss_segs[s] if not x in keys[digit1] and x in keys[digit2]]) 
    else:
      poss_segs[s] = "".join([x for x in poss_segs[s] if not x in keys[digit1] and x not in keys[digit2]]) 
    if poss_segs[s] == '':
      print("We went wrong for seg %d at comp(%d, %d)" % (s, digit1, digit2))
      sys.exit(0)

fp = open("tiny.txt", 'r')
for line in fp:
  inputs, outputs = line.strip().split('|')
  out = outputs.strip().split(" ")
  for i in range(len(out)):
    out[i] = "".join((sorted(out[i])))

  ins = inputs.strip().split(" ")
  for i in range(len(ins)):
    ins[i] = "".join(sorted(ins[i]))

  ins += out
  print ins

  key = [0]*10
  segments = [0]*7
  possible_segments = ['abcdefg'] * 7
  key[8] = 'abcdefg'

  for v in ins:
    if len(v) == 2:
      key[1] = v
    elif len(v) == 3:
      key[7] = v
    elif len(v) == 4:
      key[4] = v
        

  done = False
  while not done:
    if key[1] != 0:
      do_update(1, key[1], possible_segments)
      print "updated based on 1: ", possible_segments

    if key[7] != 0:
      do_update(7, key[7], possible_segments)
      print "updated based on 7: ", possible_segments
      
    if key[4] != 0:
      do_update(4, key[4], possible_segments)
      print "updated based on 4: ", possible_segments

    for x in range(len(key)):
      for y in range(x + 1, len(key)):
        if key[x] != 0 and key[y] != 0:
          print "Compare:", x, y, "; key: ", key
          compare(x, y, key, possible_segments)
          print "updated based on compare ", possible_segments

    for x in range(len(key)):
      if key[x] == 0:
        l = []
        # union segments that are in mapping
        for s in mapping[x]:
          print "Check mapping for segment", s, possible_segments[s]
          for p in possible_segments[s]:
            if p not in l:
              l.append(p)
        l = "".join(sorted(l))
        if len(l) == len(mapping[x]):
          key[x] = l
          print "Discovered", x, "key: ", l
          do_upate(x, key[x], possible_segments)
        else:
          print "Segments: ", l, "; mapping: ", mapping[x]
    print key
    done = True

  for o in range(len(out)):
    for k in range(len(key)):
      if out[o] == key[k]:
        out[o] = k
  print out
     

  print key
  sys.exit(0)
