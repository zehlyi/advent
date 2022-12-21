
tchars = 0
tcode = 0

f = open('input.txt', 'r')
for line in f:
  line = line.strip()
  chars = 0
  code = len(line)
  i = 1
  while i < len(line) - 1:
    if line[i] != '\\':
      i += 1
      chars += 1
      continue
    if line[i+1] != 'x':
      chars += 1
      i += 2 
      continue
    chars += 1
    i += 4
  #print line, code, chars
  tcode += code
  tchars += chars

print tcode - tchars
