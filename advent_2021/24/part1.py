import sys

program = []

memo = []
for i in range(14):
  memo.append({})
memoized = [0]*14
curr = [0]*14

def run_to_next_inp(inp, start_inst, start_vars):
  i = start_inst
  var = {}
  for k in start_vars.keys():
    var[k] = start_vars[k]
  op = program[i][0]
  if op != 'inp':
    print i
    print "aaah"
    print program[i]
    sys.exit(0)
  a = program[i][1]
  var[a] = inp
  
  i += 1
  while i < len(program):
    inst = program[i]
    i += 1
    op = inst[0]
    if op == 'inp':
      return [i - 1, var]

    a, b = inst[1:]
    if b >= 'w' and b <= 'z':
      b = var[b]
    else:
      b = int(b)
    
    if op == 'add':
      var[a] = var[a] + b
      continue
    elif op == 'mul':
      var[a] = var[a] * b
      continue
    elif op == 'div':
      if b == 0:
        return False
      var[a] = var[a] / b
      continue
    elif op == 'mod':
      if b == 0:
        return False
      var[a] = var[a] % b
      continue
    elif op == 'eql':
      var[a] = 1 if var[a] == b else 0

  # Maybe we're the last digit
  return [i - 1, var]

def run_to_next2_inp(inp, start_inst, start_vars):
  a, b = [int(x) for x in str(inp)]
  end = run_to_next_inp(a, start_inst, start_vars)
  if not end:
    return False
  end_inst, end_var = end
  return run_to_next_inp(b, end_inst, end_var) 

def hashv(var):
  return var['z'] 

def check(d, v, s, inst):
  end_inst = False
  h = hashv(v)
  if s < 4:
    curr[s] = d
  if s == 3:
    print "Step 7, curr is ", curr
  if h not in memo[s]:
    memo[s][h] = ["Foo"] * 100
  if memo[s][h][d] == "Foo":
    end = run_to_next2_inp(d, inst, v)
    if not end:
      return None
    end_inst, end_var = end
    memo[s][h][d] = end_var
  else:
    memoized[s] += 1
  if s == 6:
    if not memo[s][h][d]:
      return False
    if memo[s][h][d]['z'] == 0:
      print "Found it"
      return True
    return False
  if not memo[s][h][d]:
    return False
  # Caculate the next digit
  #print m, memo[s][h][d], s+1
  for i in range(89):
    if (99 - i) % 10 == 0:
      continue
    if check(99 - i, memo[s][h][d], s+1, end_inst):
      return True
  return False 

fp = open("input.txt", 'r')
for line in fp:
  program.append(line.strip().split(' '))

var = {'w' : 0, 'x' : 0, 'y' : 0, 'z' : 0}
for i in range(89):
  if check(99 - i, var, 0, 0):
    break
