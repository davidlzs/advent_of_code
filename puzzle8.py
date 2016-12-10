screen_width = 50 #7
screen_height = 6 #3
screen = []

for r in range(0, screen_height):
    screen.append([])
    for c in range(0, screen_width):
        screen[r].append(0)

def display(s):
    for r in range(0, screen_height):
        row = ''
        for c in range(0, screen_width):
            row = row + ('#' if s[r][c] == 1 else '.')
        print(row)
        
            
def parse_command(c):
    c = c.strip()
    command = None
    if c.startswith('rect'):
        t = c.split(' ')[1].split('x')
        command = ('rect', int(t[1]) , int(t[0]))
    elif c.startswith('rotate column'):
        t = c.split(' ')
        col = int(t[2].split('=')[1])
        move = int(t[4])
        command = ('rotate column', col , move)
    elif c.startswith('rotate row'):
        t = c.split(' ')
        row = int(t[2].split('=')[1])
        move = int(t[4])
        command = ('rotate row', row , move)
    return command

def exec_command(c, screen):
    if c[0] == 'rect':
        x1 = c[1]
        y1 = c[2]
        for r in range(0, x1):
            for c in range(0, y1):
                screen[r][c] = 1
    elif c[0] == 'rotate column':
        col = c[1]
        move = c[2]
        final_col = [0] * screen_height
        start_col = [screen[r][col] for r in range(0, screen_height)] 
        for r in range(0, screen_height):
            if start_col[r] == 1:
                final_pos = (r + move) % screen_height
                final_col[final_pos] = 1

        for r in range(0, screen_height):
            screen[r][col] = final_col[r]
    elif c[0] == 'rotate row':
        row = c[1]
        move = c[2]
        final_row = [0] * screen_width
        start_row = [screen[row][c] for c in range(0, screen_width)] 
        for c in range(0, screen_width):
            if start_row[c] == 1:
                final_pos = (c + move) % screen_width
                final_row[final_pos] = 1

        for c in range(0, screen_width):
            screen[row][c] = final_row[c]
        
    display(screen)

    

with open('puzzle8_input.txt') as f:
    content = f.readlines()
    for line in content:
        print(line)
        command = parse_command(line)
        print(command)
        exec_command(command, screen)

    cnt = 0
    for r in range (0, screen_height):
        for c in range(0, screen_width):
            if screen[r][c] == 1:
                cnt = cnt + 1
    print('_____________________')            
    display(screen)
    print('lit up', cnt)


