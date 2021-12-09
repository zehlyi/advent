import sys

fp = open("input_sort.txt", 'r')

a = []
arr = []

for line in fp:
  bits = line.strip()
  a.append(bits)
  arr.append(bits)

# oxygen
b = 0
while len(a) > 1:
  pivot = (len(a)) / 2
  p = a[pivot]
  #print("index %d, pivot %s, bit: %s" % (pivot, p, p[b]))
  if p[b] == '0':
    # 0 is more common. Drop all ones. Find the first one:
    x = max(pivot-1, 0)
    while x < len(a) and a[x][b] == '0':
      x += 1
#    print("On bit %d, found first uncommon (1): %s" % (b, a[x]))
    a = a[:x]
  else:
    x = min(pivot+1, len(a)-1)
    while x >= 0 and a[x][b] == '1':
      x -= 1
#    print("On bit %d, found first uncommon (0): %s" % (b, a[x]))
    a = a[x+1:]
  b += 1
#  print a
     
print a 
  
# CO2 
b = 0
while len(arr) > 1:
  pivot = (len(arr)) / 2
  p = arr[pivot]
  #print("index %d, pivot %s, bit: %s" % (pivot, p, p[b]))
  if p[b] == '1':
    # 0 is less common. Drop all ones. Find the first one:
    x = min(pivot+1, len(arr)-1)
    while x >= 0 and arr[x][b] == '1':
      x -= 1 
    print("On bit %d, found first common (1): %s" % (b, arr[x]))
    arr = arr[:x+1]
  else:
    x = max(pivot, 0)
    while x < len(arr) and arr[x][b] == '0':
      x += 1
    print("On bit %d, found first common (0): %s" % (b, arr[x]))
    arr = arr[x:]
  b += 1
  print len(arr)
  print arr

print arr
