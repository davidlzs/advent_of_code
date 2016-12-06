chars = None
with open('puzzle6_input.txt') as f:
    content = f.readlines()
    print(content)
    for line in content:
        if chars == None:
            chars = {}
            for i in range (0, len(line) -1):
                chars[i] = {}
        for idx, c in enumerate(line.strip()):
            chars[idx][c] = chars[idx].get(c, 0) + 1
            #print("idx, c, chars", idx, c, chars[idx])
result  = []
for i, cnt in chars.items():
    chars_list = [(k, v) for k, v in cnt.items()]
    chars_list = sorted(chars_list, key = lambda x: x[1], reverse = True)
    
    print(chars_list)
    print (i, chars_list[-1][0])

