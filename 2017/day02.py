from common import Input
import itertools

matrix = []

for line in Input(2):
    line = line.strip().split()
    matrix.append([int(x) for x in line])

total = 0

for line in matrix:
    total += max(line) - min(line)
print(total)

total = 0
for row in matrix:
    for a, b in itertools.combinations(row, 2):
        if a % b == 0:
            total += a // b
            break
        elif b % a == 0:
            total += b // a
            break

print(total)
