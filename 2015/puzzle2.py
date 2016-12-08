def calc_areas(edges):
    a = edges[0]
    b = edges[1]
    c = edges[2]
    area1 = a * b
    area2 = b * c
    area3 = c * a
    areas = [area1, area2, area3] 
    areas = sorted(areas)
    total = 2 * sum(areas) + areas[0] 
    return total
def find_edges(s):
    edges = [int(e) for e in s.strip().split('x')]
    return edges
def calc_ribbon(edges):
    edges = sorted(edges)
    return 2 * (edges[0] + edges[1]) + edges[0] * edges[1] * edges[2]
    
with open('puzzle2_input.txt') as f:
    content = f.readlines();
    total = 0
    total_ribbon = 0
    for line in content:
        edges = find_edges(line)
        total = total + calc_areas(edges)
        total_ribbon = total_ribbon + calc_ribbon(edges)
    print('Total wrapper', total)
    print('Total ribbon', total_ribbon)
