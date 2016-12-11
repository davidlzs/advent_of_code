from functools import reduce
import operator
with open('ride.in') as f:
    name = reduce(operator.mul, [(ord(c) - 64) for c in f.readline().strip()], 1) % 47
    group = reduce(operator.mul, [(ord(c) - 64) for c in f.readline().strip()], 1) % 47
    with open('ride.out', 'w') as o:
        if name == group:
            o.write('GO\n')
        else:
            o.write('STAY\n')
    print(name, group)
    
