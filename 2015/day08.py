import re
from common import input

original = in_mem = 0
for line in input(8):
    line = bytes(line.strip(), 'UTF8')
    original += len(line)
    in_mem += len(eval(line))

print(original - in_mem)

new = 0
for line in input(8):
    line = bytes(line.strip(), 'UTF8')
    new += len(re.escape(line)) + 2

print(new - original)
