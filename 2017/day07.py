from common import Input
import re


class Node:
    def __init__(self, name, weight):
        self.name = name
        self.weight = weight
        self.children = []


class UnbalancedTree(Exception):
    pass


def build_tree(base, parents, weights):
    tree = Node(base, weights[base])
    for n in (name for name, p in parents.items() if p == base):
        tree.children.append(build_tree(n, parents, weights))
    return tree


def weigh_balanced_tree(tree):
    if not tree.children:
        return tree.weight

    weights = {n: weigh_balanced_tree(n) for n in tree.children}
    weights_list = list(weights.values())
    if all(w == weights_list[0] for w in weights_list):
        return tree.weight + sum(weights_list)

    weight_count = lambda x: weights_list.count(x)
    odd_weight, correct_weight, *_ = sorted(weights_list, key=weight_count)
    diff = odd_weight - correct_weight
    odd_child = [w for w in weights if weights[w] == odd_weight][0]
    message = 'Tree is unbalanced: "{}" weighs {}, but should weigh {}.'
    message = message.format(odd_child.name, odd_child.weight, odd_child.weight - diff)
    raise UnbalancedTree(message)


if __name__ == '__main__':
    parent = {}
    weight = {}

    for line in Input(7):
        m = re.match(r'^(\w+) \((\d+)\)(?: -> (.*))?$', line)
        name, w, children = m.groups()
        weight[name] = int(w)
        if name not in parent:
            parent[name] = None
        if not children: continue
        for c in children.split(', '):
            parent[c] = name

    base = [n for n in parent if parent[n] is None][0]
    print('Base Program:', base)

    tree = build_tree(base, parent, weight)
    try:
        w = weigh_balanced_tree(tree)
    except UnbalancedTree as e:
        print(e)
    else:
        print('Tree weighs', w)
