from common import Input

s = Input(1).read().strip()
numbers = []
for i, n in enumerate(s):
    if s[i - 1] == n:
        numbers.append(n)

print(sum(int(x) for x in numbers))

numbers = []
for i, n in enumerate(s):
    opposite = (i + len(s) // 2) % len(s)
    if s[opposite] == n:
        numbers.append(n)

print(sum(int(x) for x in numbers))
