directions_dir = {'N': {'L':'W', 'R':'E'}, 'E':{'L': 'N', 'R': 'S'}, 'S':{'L':'E', 'R':'W'}, 'W':{'L':'S', 'R':'N'}}

steps_str = 'L4, R2, R4, L5, L3, L1, R4, R5, R1, R3, L3, L2, L2, R5, R1, L1, L2, R2, R2, L5, R5, R5, L2, R1, R2, L2, L4, L1, R5, R2, R1, R1, L2, L3, R2, L5, L186, L5, L3, R3, L5, R4, R2, L5, R1, R4, L1, L3, R3, R1, L1, R4, R2, L1, L4, R5, L1, R50, L4, R3, R78, R4, R2, L4, R3, L4, R4, L1, R5, L4, R1, L2, R3, L2, R5, R5, L4, L1, L2, R185, L5, R2, R1, L3, R4, L5, R2, R4, L3, R4, L2, L5, R1, R2, L2, L1, L2, R2, L2, R1, L5, L3, L4, L3, L4, L2, L5, L5, R2, L3, L4, R4, R4, R5, L4, L2, R4, L5, R3, R1, L1, R3, L2, R2, R1, R5, L4, R5, L3, R2, R3, R1, R4, L4, R1, R3, L5, L1, L3, R2, R1, R4, L4, R3, L3, R3, R2, L3, L3, R4, L2, R4, L3, L4, R5, R1, L1, R5, R3, R1, R3, R4, L1, R4, R3, R1, L5, L5, L4, R4, R3, L2, R1, R5, L3, R4, R5, L4, L5, R2'
def register_all_visited(visited, move_direction, start_x, start_y, steps):
    for s in range(1, steps + 1):
        if move_direction == 'E':
            register_visited_point(visited, start_x + s, start_y)
    
        if  move_direction == 'S':
            register_visited_point(visited, start_x, start_y - s)

        if  move_direction == 'W':
            register_visited_point(visited, start_x - s, start_y)

        if  move_direction == 'N':
            register_visited_point(visited, start_x, start_y + s)

def register_visited_point(visited, x, y):
    global head_quarter
    key = str(x) + '_' + str(y)
    if visited.get(key) == None:
        visited[key] = 1
    else:
        visited[key] += 1
        if head_quarter == None:
            head_quarter = key


head_quarter = None
steps = steps_str.split(', ')
print(steps)
#steps = [int(s[1:]) for s in steps]
visited = {'0_0': 1}
current_face = 'N'
x = 0
y = 0
for s in steps:
    move_direction = directions_dir[current_face][s[0]]
    move_steps = int(s[1:])
    if move_direction == 'E':
        new_y = y
        new_x = x + move_steps
    elif move_direction == 'S':
        new_x = x
        new_y = y - move_steps
    elif move_direction == 'W':
        new_x = x - move_steps
        new_y = y
    elif move_direction == 'N':
        new_x = x
        new_y = y + move_steps

    register_all_visited(visited, move_direction, x, y, abs(move_steps))

    current_face = move_direction
    x = new_x
    y = new_y
    print('Current face', current_face, 'turning', s[0], " then face", move_direction, 'x', x, 'y', y)

total_dist = abs(x) + abs(y)
print('Total distance', total_dist)

header_quarter_loc =head_quarter.split('_')
x_head_quarter = int(header_quarter_loc[0])
y_head_quarter = int(header_quarter_loc[1])
head_quarter_dist = abs(x_head_quarter) + abs(y_head_quarter)
print('Head Quarter distance', head_quarter_dist)




