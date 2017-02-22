from collections import namedtuple
import re
from itertools import combinations
from pprint import pprint

shop = '''Weapons:    Cost  Damage  Armor
Dagger        8     4       0
Shortsword   10     5       0
Warhammer    25     6       0
Longsword    40     7       0
Greataxe     74     8       0

Armor:      Cost  Damage  Armor
Leather      13     0       1
Chainmail    31     0       2
Splintmail   53     0       3
Bandedmail   75     0       4
Platemail   102     0       5

Rings:      Cost  Damage  Armor
Damage +1    25     1       0
Damage +2    50     2       0
Damage +3   100     3       0
Defense +1   20     0       1
Defense +2   40     0       2
Defense +3   80     0       3
'''

Gear = namedtuple('Gear', 'name, cost, damage, armor')


def parse_shop(shop):
    shop = shop.split('\n\n')
    d = {}
    for category in shop:
        cname = category.split(':')[0]
        d[cname] = [Gear('None', 0, 0, 0)]  # pre-seed with None, all gear is optional
        for line in category.splitlines():
            line = line.strip()
            if 'Cost' in line or not line:
                continue
            else:
                g = re.split(r'\s{2,}', line)
                print(g)
                g[1:] = map(int, g[1:])
                d[cname].append(Gear(*g))

    #pre-combine the possible rings to cut down on iterations
    d['Weapons'] = d['Weapons'][1:]  # must have a weapon
    d['Rings'].append(Gear('None', 0, 0, 0))  # need extra null ring for no ring case
    d['Rings'] = list(combinations(d['Rings'], 2))
    return d


def all_gear_combos(gear):
    for weapon in gear['Weapons']:
        for armor in gear['Armor']:
            for r1, r2 in gear['Rings']:
                yield (weapon, armor, r1, r2)


def stats(loadout):
    c = sum(l.cost for l in loadout)
    d = sum(l.damage for l in loadout)
    a = sum(l.armor for l in loadout)
    return c, d, a


def victory(player, boss):
    ps = needed_swings(player, boss)
    bs = needed_swings(boss, player)
    if bs < ps:
        return False
    else:
        return True


def needed_swings(a, b):
    _, dam, _ = a
    b_hp, _, b_arm = b
    dps = dam - b_arm
    dps = 1 if dps < 1 else dps
    needed_swings = b_hp // dps
    if b_hp % dps != 0:
        needed_swings += 1
    return needed_swings


def make_player(loadout):
    _, d, a = stats(loadout)
    return (100, d, a)


def simulate(player, boss):
    hp, dam, arm = player
    b_hp, b_dam, b_arm = boss
    player_turn = True
    # print(hp, b_hp)
    while b_hp > 0 and hp > 0:
        if player_turn:
            s = dam - b_arm
            s = 1 if s < 1 else s
            b_hp -= s
        else:
            s = b_dam - arm
            s = 1 if s < 1 else s
            hp -= s
        # print(hp, b_hp)
        player_turn = not player_turn

    if hp > 0 and b_hp <= 0:
        print('player wins!')
        return True
    else:
        print('boss wins!')
        return False


if __name__ == '__main__':
    gear = parse_shop(shop)
    boss = 103, 9, 2
    min_gear = max((g for g in all_gear_combos(gear)
                    if not victory(make_player(g), boss)),
                   key=stats)
    print(min_gear)
    print(stats(min_gear))
    player = make_player(min_gear)
    assert not victory(player, boss)
    print(needed_swings(boss, player))
    print(needed_swings(player, boss))
    assert not simulate(player, boss)
