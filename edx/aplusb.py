with open('aplusb.in') as f:
    a, b = map(int, f.readline().strip().split(' '))
    with open('aplusb.out', 'w') as o:
        o.write(str(a+b))
