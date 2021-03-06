triangles = {}
def is_triangle(edges):
    edges = sorted(edges)
    return edges[0] + edges[1] > edges[2]

lines = []
with open('puzzle3_input.txt') as f:
    content = f.readlines()
    for line in content:
        a = int(line[:5].strip())
        b = int(line[6:10].strip())
        c =  int(line[11:15].strip())
        result = is_triangle([a, b, c])
        lines.append(result)
    triangle_count = len([r for r in lines if r])
    print('True Triangle', triangle_count)

column_lines = []
with open('puzzle3_input.txt') as f:
    content = f.readlines()
    i = 0
    size = len(content)
    while i < size:
        line1 = content[i][:-1]
        line2 = content[i+1][:-1]
        line3 = content[i+2][:-1]
        a1 = int(line1[:5].strip())
        b1 = int(line2[:5].strip())
        c1 = int(line3[:5].strip())
        result = is_triangle([a1, b1, c1])
        column_lines.append(result)

        a2 = int(line1[6:10].strip())
        b2 = int(line2[6:10].strip())
        c2 = int(line3[6:10].strip())
        result = is_triangle([a2, b2, c2])
        column_lines.append(result)
        
        a3 = int(line1[11:15].strip())
        b3 = int(line2[11:15].strip()) 
        c3 = int(line3[11:15].strip()) 
        result = is_triangle([a3, b3, c3])
        column_lines.append(result)
        i += 3
    triangle_count = len([r for r in column_lines if r])
    print('True Triangle', triangle_count)
