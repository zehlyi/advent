
total = 0
seen_freqs = set()
seen_freqs.add(total)
it = 0
while True:
  print "Iteration:", it
  f = open('input1.txt', 'r')
  for line in f:
    total += int(line.strip())
    print total
    if total in seen_freqs:
      print total
      sys.exit(0)
    seen_freqs.add(total)
  it += 1
