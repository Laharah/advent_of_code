from collections import namedtuple
from my_utils.graphs import Path, heappop, heappush
from pprint import pprint
from copy import deepcopy


class State:
    PLAYER_MOVES = { # mana cost must be first
        'Magic Missile': [('mana', -53), ('boss_hp', -4)],
        'Drain': [('mana', -73), ('boss_hp', -2), ('hp', 2)],
        'Shield': [('mana', -113), ('armor', 7), ('effects', ('Shield', 6))],
        'Poison': [('mana', -173), ('effects', ('Poison', 6))],
        'Recharge': [('mana', -229), ('effects', ('Recharge', 5))]
    }
    Effects = { # (on, out)
        'Shield': ((), ('armor', -7)),
        'Poison':(('boss_hp', -3), ()),
        'Recharge':(('mana', 101), ())
    }

    MANA_COST = {k: v[0][1]*-1 for k, v in PLAYER_MOVES.items()}
    MANA_COST['Boss Attack'] = 0

    def __init__(self, hp=50,
                 mana=500,
                 armor=0,
                 boss_hp=58,
                 boss_damage=9,
                 effects=None,
                 turn=True):
        self.hp = hp
        self.mana = mana
        self.armor = armor
        self.boss_hp = boss_hp
        self.boss_damage = boss_damage
        self.effects = deepcopy(effects) if effects else []
        self.turn = turn

    def after(self, move):
        s = self.__class__(self.hp, self.mana, self.armor, self.boss_hp, self.boss_damage,
                           self.effects, self.turn)

        s._apply_move(move)

        s.turn = not self.turn
        if not s.turn:
            s.hp -= 1

        s._evaluate_effects()

        return s

    def get_moves(self):
        if self.boss_hp <= 0 or self.hp <= 0:
            return []
        if not self.turn:
            return ["Boss Attack"]

        valid_moves = []
        current_effects = {e[0] for e in self.effects}
        for m in self.PLAYER_MOVES:
            if self.MANA_COST[m] <= self.mana:
                if m not in current_effects:
                    valid_moves.append(m)
        return valid_moves

    def _apply_move(self, move):
        if self.turn:
            for a, delta in self.PLAYER_MOVES[move]:
                self._do_action(a, delta)
        else:
            d = self.boss_damage - self.armor
            self.hp -= 1 if d < 1 else d

    def _do_action(self, attrib, delta):
        if isinstance(delta, tuple):
            old = self.__getattribute__(attrib)
            old.append(delta)
            self.__setattr__(attrib, old)
        else:
            new = self.__getattribute__(attrib) + delta
            self.__setattr__(attrib, new)

    def _evaluate_effects(self):
        new_effects = []
        for name, time in self.effects:
            on, out = self.Effects[name]
            if on: self._do_action(*on)
            time -= 1
            if time == 0:
                if out: self._do_action(*out)
            else:
                new_effects.append((name, time))
        self.effects = new_effects

    def __eq__(self, other):
        return self is other

    def __lt__(self, other):
        return id(self) < id(other)

    def __hash__(self):
        return id(self)

    def __repr__(self):
        st = '{}(hp={s.hp}, mana={s.mana}, armor={s.armor}, boss_hp={s.boss_hp}, boss_damage={s.boss_damage}, effects={s.effects}, turn={s.turn})'
        return st.format(self.__class__.__name__, s=self)


def estimate_cost(state):
    'ideal cost, sum of manacost of cheapest spell to kill boss'
    if state.boss_hp <= 0 and state.hp > 0 :
        return 0
    # else: # do bfs
    #     return 1

    # assume poisoned, and eating a magic missile each turn
    return state.boss_hp//7 * 53 or 53

def astar_search(start, h_func, moves_func):
    """
       returns the shortest path from start to state where h_func == 0,
           or None if path cannot be found.

           h_func: huristic function, must return 0 for goal. A bfs function
             is provided in this module to turn a_star into a breadth first search.
           moves_func: given node, get the available moves from that node
           cost_func: given 2 nodes, returns the cost of that edge, defaults to 1
    """
    frontier = [(h_func(start), start)]
    parent = {start: None}
    path_cost = {start: 0}
    best_move = {}

    while frontier:
        h, node = heappop(frontier)
        if h_func(node) == 0:
            return Path(parent, node), best_move, path_cost[node]
        for move in moves_func(node):
            neighbor = node.after(move)
            new_cost = path_cost[node] + node.MANA_COST[move]
            estimated = h_func(neighbor)
            if neighbor not in path_cost or new_cost + estimated < path_cost[neighbor]:
                heappush(frontier, (new_cost + estimated, neighbor))
                path_cost[neighbor] = new_cost
                best_move[neighbor] = move
                parent[neighbor] = node
    return None

if __name__ == '__main__':
    s = State(hp=10, mana=250, boss_hp=13, boss_damage=8)
    assert s.get_moves() == list(s.PLAYER_MOVES), s.get_moves()
    s = s.after('Poison')
    assert s.mana == 77, s.mana
    assert s.effects == [('Poison', 5)], s
    assert s.boss_hp == 10
    assert s.get_moves() == ['Boss Attack']
    s = s.after('Boss Attack')
    assert s.hp == 1
    assert s.boss_hp == 7
    assert s.turn
    assert s.get_moves() == ['Magic Missile', 'Drain']

    real = State(hp=50, mana=500, boss_hp=58, boss_damage=9)
    test = State(hp=10, mana=250, boss_hp=13, boss_damage=8)
    moves = lambda s: s.get_moves()


    path, moves, cost= astar_search(real, h_func=estimate_cost, moves_func=moves)
    total = 0
    for p in path:
        try:
            print(moves[p])
            total += real.MANA_COST[moves[p]]
        except KeyError:
            pass
        print(p)
    print(cost)
