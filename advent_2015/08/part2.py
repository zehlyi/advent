
tchars = 0
tcode = 0

f = open('input.txt', 'r')
for line in f:
  line = line.strip()
  chars = len(line)
  # First and last quote
  code = chars + 2
  for c in line:
    if c == '"':
      code += 1
    elif c == '\\':
      code += 1
  #print line, code, chars
  tcode += code
  tchars += chars

print tcode - tchars
