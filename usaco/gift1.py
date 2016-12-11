import collections
from functools import reduce
import operator

Giving = collections.namedtuple('Giving', 'giver allowance n_to tos')


def give(balances, givings):
    for g in givings:
        if g.n_to > 0:
            average_amt = int(g.allowance / g.n_to)
            balances[g.giver] = balances[g.giver] + g.allowance % g.n_to
            for t in g.tos:
                balances[t] = balances[t] + average_amt

    for g in givings:
        balances[g.giver] =   balances[g.giver] - g.allowance

with open('gift1.in') as f:
    np = int(f.readline().strip())
    players = []
    givings = []
    for i in range(0, np):
        players.append(f.readline().strip())
    for i in range(0, np):
        name = f.readline().strip()
        allowance, number_to = [int(e) for e in f.readline().strip().split()]
        tos = []
        for j in range(0, number_to):
            tos.append(f.readline().strip())
        givings.append(Giving(name, allowance, number_to, tos))
    print(np, players)
    print(givings)
    balances = {g.giver:0 for g in givings}
    print(balances)
    give(balances, givings)
    print(balances)

