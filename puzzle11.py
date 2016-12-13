import collections
import itertools
import copy

State = collections.namedtuple('State', 'snapshot elevator')
Move = collections.namedtuple('Move', 'from_level to_level stuffs')

def is_safe(stuff, target_stuff):
    all_stuff = stuff + elements(target_stuff)
    all_m = [m for m in all_stuff if m.endswith('M')]
    all_g = [g for g in all_stuff if g.endswith('G')]
    matches = []
    for m in all_m:
        for g in all_g:
            if m[0] == g[0]:
                matches.append(m[0])
    not_matched_m = [m for m in all_m if m[0] not in matches]
    not_matched_g = [g for g in all_g if g[0] not in matches]
    #return not (len(not_matched_m) > 0 and len(not_matched_g))
    return not (len(not_matched_m) > 0 and len(all_g) > 0)
    
def valid_on_elevator(current_stuff):
    current_stuff = elements(current_stuff)
    ones = list(itertools.combinations(current_stuff, 1))
    twos = [e for e in list(itertools.combinations(current_stuff, 2)) if ((e[0][1] == e[1][1]) or (e[0][0] == e[1][0]))]
    return ones + twos
    

def display(s):
    for r in reversed(s):
        print(''.join(r))        

def display_states(ss):
    for s in ss:
        print('------------------')
        display(s.snapshot)

def elements(eles):
    return [i for i in eles[1:] if i != '. ']

def is_waste(s, e, direction):
    if len(e) == 1 and direction == 'up' and s.elevator < 3:
        for i in range(s.elevator + 1, 3):
            if len(elements(s.snapshot[i])) > 0:
                return False
        return True
    elif len(e) == 1 and direction == 'down' and s.elevator > 0:
        for i in range(0, s.elevator - 1):
            if len(elements(s.snapshot[i])) > 0:
                return False
        return True
    return False



def is_done(ss):
    for s in ss:
        if '. ' not in s.snapshot[3]:
            return True

#start_snapshot = [
#    ['E ', '. ', 'HM', '. ', 'LM'],
#    ['. ', 'HG', '. ', '. ', '. '],
#    ['. ', '. ', '. ', 'LG', '. '],
#    ['. ', '. ', '. ', '. ', '. ']
#    ] 
start_snapshot = [
    ['E ', 'SG', 'SM', 'PG', 'PM', '. ', '. ', '. ', '. ', '. ', '. '],
    ['. ', '. ', '. ', '. ', '. ', 'TG', '. ', 'RG', 'RM', 'CG', 'CM'],
    ['. ', '. ', '. ', '. ', '. ', '. ', 'TM', '. ', '. ', '. ', '. '],
    ['. ', '. ', '. ', '. ', '. ', '. ', '. ', '. ', '. ', '. ', '. ']
    ] 

columns = {}
for r in start_snapshot:
    for x in [(e, idx) for idx, e in enumerate(r) if e != '. ']:
        columns[x[0]] = x[1]
    
print(columns)
start_state = State(start_snapshot, 0)

moves = 0
states = [start_state]
visited = [start_state]
found = False
while not found:
    to_be_states = []
    for s in states:
        c = s.snapshot[s.elevator]
        v = valid_on_elevator(c)
#        print('+++++++++++++++++++++++++++++++++++++++')
#        display(s.snapshot)
#        print('valid moves for', moves, v)
#        print('+++++++++++++++++++++++++++++++++++++++')
        for e in v:
            # move up
            if s.elevator + 1 <= 3:
                s1 = copy.deepcopy(s)
                t = s.snapshot[s.elevator + 1]
                if is_safe(list(e), t) and not is_waste(s, e, 'up'): 

                    for e1 in e:
                        s1.snapshot[s.elevator + 1][columns[e1]] = e1
                        s1.snapshot[s.elevator][columns[e1]] = '. '
                        s1.snapshot[s.elevator + 1][0] = 'E '
                        s1.snapshot[s.elevator][0] = '. '
                        s1 = State(s1.snapshot, s.elevator + 1)
                    if s1 not in visited: 
                        #print('FROM:')
                        #display(s.snapshot)
                        #print('up',moves, e, t)
                        #print('TO:')
                        #display(s1.snapshot)
                        #print('======================')
                        to_be_states.append(s1)
                        visited.append(s1)
            # move down
            if s.elevator - 1 >= 0:
                s1 = copy.deepcopy(s)
                t = s.snapshot[s.elevator - 1]
                if is_safe(list(e), t) and not is_waste(s, e, 'down'): 
                    for e1 in e:
                        s1.snapshot[s.elevator - 1][columns[e1]] = e1
                        s1.snapshot[s.elevator][columns[e1]] = '. '
                        s1.snapshot[s.elevator - 1][0] = 'E '
                        s1.snapshot[s.elevator][0] = '. '
                        s1 = State(s1.snapshot, s.elevator - 1)
                    if s1 not in visited: 
                        #print('FROM:')
                        #display(s.snapshot)
                        #print('down',moves, e, t)
                        #print('TO:')
                        #display(s1.snapshot)
                        #print('======================')
                        to_be_states.append(s1)
                        visited.append(s1)
    moves = moves + 1        
    print("moves in" , moves, len(to_be_states), len(visited))
    states = to_be_states
    
    found = is_done(states) 
print('moves', moves)



