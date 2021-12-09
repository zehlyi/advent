import sys

fp = open("input.txt", 'r')

bits = []

for line in fp:
  s = line.strip()
  for c in range(len(s)):
    if c == len(bits):
      bits.append(0)
    bits[c] += -1 if int(s[c]) == 0 else 1

for b in bits:
  print("%d" % 0 if b < 0 else 1)
