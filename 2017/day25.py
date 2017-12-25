import re
from collections import defaultdict, namedtuple
from common import Input

State = namedtuple('State', 'name, action_false, action_true')


def setup():
    start = 'A'
    diagnostic = 12481997

    state = {
        'A': State('A', (1, 1, 'B'), (0, -1, 'C')),
        'B': State('B', (1, -1, 'A'), (1, 1, 'D')),
        'C': State('C', (0, -1, 'B'), (0, -1, 'E')),
        'D': State('D', (1, 1, 'A'), (0, 1, 'B')),
        'E': State('E', (1, -1, 'F'), (1, -1, 'C')),
        'F': State('F', (1, 1, 'D'), (1, 1, 'A')),
    }

    return start, diagnostic, state


def run(start, diagnostic, state):
    s = start
    i = 0
    tape = defaultdict(int)
    for _ in range(diagnostic):
        st = state[s]
        write, move, next_state = st[tape[i] + 1]
        tape[i] = write
        i += move
        s = next_state
    return tape


if __name__ == '__main__':
    start, diag, state = setup()
    print(sum(run(start, diag, state).values()))
