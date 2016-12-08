def find_floor(s):
    level = 0
    for idx, c in enumerate(s):
        if c == '(':
            level = level + 1
        elif c == ')':
            level = level - 1
        if level == -1:
            print('index is: ', idx + 1, level)
    return level

with open('puzzle1_input.txt') as f:
    content = f.readlines();
    print('Level', find_floor(content[0]))

