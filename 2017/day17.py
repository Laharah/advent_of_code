class Node:
    'Circular linked list node class'

    def __init__(self, data):
        self.data = data
        self.next = self

    def __iter__(self):
        runner = self
        yield runner
        runner = self.next
        while runner != self:
            yield runner
            runner = runner.next


def print_buffer(head, runner=None):
    'prints the buffer, for debugging purposes'
    listified = list(
        str(x.data) if x is not runner else '({})'.format(x.data) for x in head)
    print(' '.join(listified))


def value_after(n, step_size):
    'returns the next value in order after the insertion of n'
    head = Node(0)
    runner = head
    step_size = step_size
    for i in range(1, n + 1):
        for _ in range(step_size):
            runner = runner.next
        n = Node(i)
        n.next = runner.next
        runner.next = n
        runner = n

    return runner.next.data


def get_after_zero(n, step_size):
    'returns the value at index 1 after n insertions'
    after = 0
    current_size = 1
    index = 0
    # 0 is always at index 0 so we only need to track when a value is
    # going to be inserted after index 0
    for i in range(1, n + 1):
        next_index = (index + step_size) % current_size
        if next_index == 0:
            after = i
        index = next_index + 1
        current_size += 1
    return after


if __name__ == '__main__':
    print(value_after(2017, 303))
    print(get_after_zero(50000000, 303))
