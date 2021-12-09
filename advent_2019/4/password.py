start = 367479
end = 893698

count = 0;

for i in range(start, end):
    word = str(i)
    pair = False
    increase = True
    for l in range(1, len(word)):
        if word[l] < word[l-1]:
            increase = False
            break
        if word[l] == word[l-1]:
            if (l == len(word) - 1 or word[l+1] != word[l]) and (l == 1 or word[l-2] != word[l]):
                pair = True
    if increase and pair:
        print word
        count += 1

print count
