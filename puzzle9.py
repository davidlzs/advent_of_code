import re
p = re.compile('\(\d+x\d+\)')
def decompress(l):
    result = ''
    marker = None
    repeat_str = ''

def find_markers(l):
    markers  = []
    it = p.finditer(l)
    for m in it:
        m_span = m.span()
        m_group = m.group()
        #print('m_group', m_group)
        if len(markers) > 0:
            last_marker = markers[-1]
            if last_marker[0][1] + last_marker[1][0] > int(m_span[0]):
                pass
            else:
                markers.append((m_span, parse_marker(m_group), m_group))
    #        print('last marker', last_marker)
        else:
            markers.append((m_span, parse_marker(m_group), m_group))
        #print('marker', markers[-1])
    return markers

def parse_marker(m):
    m = m[1:][:-1]
    s = m.split('x')
    return (int(s[0]), int(s[1]))

def decompress(line):
    markers = find_markers(line)
    print('markers', markers)
    s = ''
    if len(markers) == 0:
        s = line
    else :
        last_pos = 0
        for m in markers:
            s = s + line[last_pos:m[0][0]]
            last_pos =m[0][1] + m[1][0] 
            repeat_str = line[m[0][1]:last_pos]
            s = s + repeat_str * m[1][1]
        s = s + line[last_pos:]

    return s

    
with open('puzzle9_sample2_input.txt') as f:
    content = f.readlines()
    for line in content:
        line = line.strip()
        print(line)
        result = decompress(line)
        print('result', '|' + result + '|', len(result))


