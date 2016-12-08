def split_line(l):
    outer_list = []
    inner_list = []
    condition = True
    open_split = l.split('[')
    for c in open_split:
        t = c.split(']')
        if len(t) == 1:
            outer_list.append(t[0])
        else:
            outer_list.append(t[1])
            inner_list.append(t[0])
    return (outer_list, inner_list)

def find_reverse_of_pairs(s):
    pairs = []
    for i in range(0, len(s) -3):
        c = s[i:i+4]
        if c[:2] == c[2:][::-1] and c[0] != c[1]:
            pairs.append(c)
    return pairs

def find_aba(s):
    abas = []
    for i in range(0, len(s) -2):
        c = s[i:i+3]
        if c[0] == c[2] and c[0] != c[1]:
            abas.append(c)
    return abas

def found(abas, outers):
    for aba in abas:
        t = aba[1] + aba[0] + aba[1] 
        for o in outers:
            if o.find(t) >=0:
                return True
    return False

    
cnt = 0
line_cnt = 1
with open('puzzle7_input.txt') as f:
    content = f.readlines()
    for line in content:
        parts = split_line(line.strip())
        print(line, parts)
        abas = []
        for p in parts[0]:
            abas.extend(find_aba(p))
        print(abas)
        if found(abas, parts[1]):
            cnt = cnt + 1
#        outer_abba_cnt = 0
#        for p in parts[0]:
#            pairs = find_reverse_of_pairs(p)
#            outer_abba_cnt = outer_abba_cnt + len(pairs)
#        if outer_abba_cnt > 0:
#            inner_abba_cnt = 0
#            for p in parts[1]:
#                pairs = find_reverse_of_pairs(p)
#                inner_abba_cnt = inner_abba_cnt + len(pairs)
#            if inner_abba_cnt == 0:
#                cnt = cnt + 1
    print('CNT', cnt)
        

