def find_rooms(s):
    visited = {'0_0': 1}
    x = 0 
    y = 0
    for c in s:
        if c == '>':
            x = x + 1
        elif c == 'v':
            y = y - 1
        elif c == '<':
            x = x - 1
        elif c == '^':
            y = y + 1
        cord_str = str(x) + '_' + str(y)
        visited[cord_str] = visited.get(cord_str, 0) + 1
    return visited
    #t = [v for v in visited.values()]
    
    #return t

with open('puzzle3_input.txt') as f:
    content = f.readlines();
    for line in content:
        s = line.strip()
        s1 = [c for i, c in enumerate(s) if i%2 == 0]
        santa_rooms = find_rooms(s1)
        s2 = [c for i, c in enumerate(s) if i%2 == 1]
        robot_rooms = find_rooms(s2)
        all_rooms = set(santa_rooms.keys()) | set(robot_rooms.keys())
        print(len(all_rooms))
