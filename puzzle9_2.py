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
    #print('markers', markers)
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
def print_markers(markers):
    for m in markers:
        print(m[2])

def calc_length(s):
    markers = find_markers(s)
    #print(markers)
    if len(markers) == 0:
        return len(s)
    else:
        parts = split_parts(markers, s)
        print('parts', parts)
        result = 0
        for part in parts:
            result = result + part[0] * calc_length(part[1])
        return result

def split_parts(ms, s):
    parts = []
    start_pos = 0
    for m in ms:
        ((start, end), (length, times), substring) = m
   #     print(start, end, length, times, substring)
        if start > start_pos:
            parts.append((1, s[start_pos:start]))
        parts.append((times, s[end:end+length]))
        start_pos = end + length
    return parts


    
with open('puzzle9_input.txt') as f:
    content = f.readlines()
    for line in content:
        line = line.strip()
        print(line)

        r = calc_length(line)
        print ('result', r)

