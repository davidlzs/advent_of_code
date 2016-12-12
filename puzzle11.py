import collections
import itertools
import copy

State = collections.namedtuple('State', 'snapshot elevator')
Move = collections.namedtuple('Move', 'from_level to_level stuffs')

def move(current_state):
    current_level = current_state.snapshot[current_state.elevator][1:]
    upper_level = None if current_state.elevator == 3 else current_state.snapshot[current_state.elevator + 1][1:]
    lower_level = None if current_state.elevator == 0 else current_state.snapshot[current_state.elevator - 1][1:]
    move_up(current_level, upper_level)
   # move_downn(current_level)
    print('upper_level  ', upper_level)
    print('current_level', current_level)
    print('lower_level  ', lower_level)

def move_up(current_level, upper_level):
    stuff = [s for s in current_level if s != '. ']
    upper_stuff = [s for s in upper_level if s != '. ']
    print('valid_on_elevator', valid_on_elevator(stuff))
    print('all stuff', stuff, upper_stuff)
    resutl = []
    #for e in valid_on_elevator(stuff):

    #if (is_safe(stuff, upper_stuff))

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
    
def move_all(states):
    result = []
    for s in states:
        result.append(move(s))

def valid_on_elevator(current_stuff):
    current_stuff = elements(current_stuff)
    ones = list(itertools.combinations(current_stuff, 1))
    twos = [e for e in list(itertools.combinations(current_stuff, 2)) if e[0][1] == 'M' and e[1][1] == 'M' or e[0][0] == e[1][0]]
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
    empty = True
    #if len(e) == 1 :
    if len(e) == 1 and direction == 'up' and s.elevator < 3:
        for i in range(s.elevator + 1, 3):
            empty = len(elements(s.snapshot[i])) > 0
            break;
        if empty:
            return empty

    elif direction == 'down' and s.elevator > 0:
        for i in range(0, s.elevator - 1):
            empty = len(elements(s.snapshot[i])) > 0
            break;
        if empty: 
            return empty
    return False



def is_done(ss):
    for s in ss:
        if '. ' not in s.snapshot[3]:
            return True

start_snapshot = [
    ['E ', '. ', 'HM', '. ', 'LM'],
    ['. ', 'HG', '. ', '. ', '. '],
    ['. ', '. ', '. ', 'LG', '. '],
    ['. ', '. ', '. ', '. ', '. ']
    ] 
#start_snapshot = [
#    ['E ', 'SG', 'SM', 'PG', 'PM', '. ', '. ', '. ', '. ', '. ', '. '],
#    ['. ', '. ', '. ', '. ', '. ', 'TG', '. ', 'RG', 'RM', 'CG', 'CM'],
#    ['. ', '. ', '. ', '. ', '. ', '. ', 'TM', '. ', '. ', '. ', '. '],
#    ['. ', '. ', '. ', '. ', '. ', '. ', '. ', '. ', '. ', '. ', '. ']
#    ] 

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
        print('current')
        display(s.snapshot)
        c = s.snapshot[s.elevator]
        for e in valid_on_elevator(c):
            # move up
            if s.elevator + 1 <= 3:
                s1 = copy.deepcopy(s)
                t = s.snapshot[s.elevator + 1]
                if is_safe(list(e), t): # and not is_waste(s, e, 'up'): 
                    print('up',moves, e, t)
                    for e1 in e:
                        s1.snapshot[s.elevator + 1][columns[e1]] = e1
                        s1.snapshot[s.elevator][columns[e1]] = '. '
                        s1.snapshot[s.elevator + 1][0] = 'E '
                        s1.snapshot[s.elevator][0] = '. '
                        s1 = State(s1.snapshot, s.elevator + 1)
                    if s1 not in visited: 
                        to_be_states.append(s1)
            # move down
            if s.elevator - 1 >= 0:
                s1 = copy.deepcopy(s)
                t = s.snapshot[s.elevator - 1]
                if is_safe(list(e), t): # and not is_waste(s, e, 'down'): 
                    print('down', moves, e, t)
                    for e1 in e:
                        s1.snapshot[s.elevator - 1][columns[e1]] = e1
                        s1.snapshot[s.elevator][columns[e1]] = '. '
                        s1.snapshot[s.elevator - 1][0] = 'E '
                        s1.snapshot[s.elevator][0] = '. '
                        s1 = State(s1.snapshot, s.elevator - 1)
                    if s1 not in visited: 
                        to_be_states.append(s1)
        visited.append(s)
    moves = moves + 1        
    display_states(to_be_states)        
    states = to_be_states
    
    found = is_done(states) 
print('moves', moves)



