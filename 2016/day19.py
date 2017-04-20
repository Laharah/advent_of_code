import math


class Dln:
    'doubly linked list Node'
    def __init__(self, data):
        self.data = data
        self.next = self
        self.prev = self

    def append(self, node):
        self.prev.next = node
        node.prev = self.prev
        self.prev = node
        node.next = self

    def die(self):
        self.prev.next = self.next
        self.next.prev = self.prev
        del self

# dlst = Dln(1)
# for i in range(2, 3004953 +1):
#     dlst.append(Dln(i))
#
# node = dlst
# while node.next is not node:
#     node.next.die()
#     node = node.next
#
# print(node.data)

def Elves(N=3004953): return list(range(1, N+1))

def one_round(elves):
    "The first third of elves eliminate ones across the circle from them; who is left?"
    N = len(elves)
    eliminated = 0
    for i in range(int(math.ceil(N / 3))):
        across = i + eliminated + (N // 2)
        elves[across] = None
        N -= 1
        eliminated += 1
    return list(filter(None, elves[i+1:] + elves[:i+1]))

def winner(elves): return (elves[0] if (len(elves) == 1) else winner(one_round(elves)))
print(winner(Elves()))
