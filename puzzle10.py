import re
import collections
from functools import reduce
import operator
p_value = re.compile('value (\d+) goes to bot (\d+)')
p_bot = re.compile('bot (\d+) gives low to (.+) (\d+) and high to (.+) (\d+)')

    
def parse_line(l):
    if l.startswith('value'):
        m = p_value.match( l )
        return ('value',) + m.groups()
    elif l.startswith('bot'):
        m = p_bot.match( l )
        return ('bot',) +  m.groups()

def move(bot_commands, tree):
    pending_commands = []
    for c in bot_commands:
        (_type, bot, low_type, low, high_type, high) = c
        if tree.get('bot' + bot) == None:
            pending_commands.append(c)
        else:
            bot_in_tree = tree['bot' + bot]

            if len(bot_in_tree) == 2:
                s = sorted(bot_in_tree)
                tree.setdefault(low_type + low, []).append(s[0])
                tree.setdefault(high_type + high, []).append(s[1])
                print('tree', tree, bot_commands)
                #move(bot_commands[1:], tree)
            else: 
                pending_commands.append(c)
    print('pending', len(pending_commands), tree)
    if len(pending_commands) > 0:
        move(pending_commands, tree)

def find_bot(tree, value_low, value_high):
    for k, v in tree.items():
        vs = sorted(v)
        if k.startswith('bot') and vs[0] == value_low and vs[1] == value_high :
            return k
def find_output123(tree):
    out = []
    for k, v in tree.items():
        if (k == 'output0' or k == 'output1' or k == 'output2'):
            out.append(Output(k, v))
    return out
Output = collections.namedtuple('Output', 'bin values')

def multiply_output(outs):
    result = 1
    for e in outs:
        bin_values_mul = reduce(operator.mul, e.values, 1) 
        result = result * bin_values_mul
    return result

tree = {}
commands = []
with open('puzzle10_input.txt') as f:
    content = f.readlines()
    for line in content:
        line = line.strip()
        #print(line)
        cmd = parse_line(line)
        #print(cmd)
        commands.append(cmd)

    #print(commands)
value_commands = [c for c in commands if c[0] == 'value']
bot_commands = [c for c in commands if c[0] == 'bot']

print('value_commands', value_commands)
print('bot_commands', bot_commands)

for c in value_commands:
    bot = c[2]
    tree.setdefault('bot' + bot, []).append(int(c[1]))

print('start' , tree)
move(bot_commands, tree)
print('final', tree)
#print(find_bot(tree, 2, 5))
print(find_bot(tree, 17, 61))
output123 = find_output123(tree)
print(output123)
print(multiply_output(output123))

            


