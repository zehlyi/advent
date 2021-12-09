import md5

seed = "yzbqklnj"
#seed = "abcdef"


c = 0
while True:
    #print md5.new(seed + str(c)).hexdigest()
    if md5.new(seed + str(c)).hexdigest()[0:6] == "000000":
        print c, md5.new(seed+str(c)).hexdigest()
        sys.quit(0)
    c += 1
