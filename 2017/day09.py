from common import Input
import re

data = Input(9).read()
data = re.sub(r'!.', '', data)

level = 0
score = 0
garbage_count = 0
not_garbage = True
i = 0
while i < len(data):
    c = data[i]
    if c == '<' and not_garbage:
        not_garbage = False
        garbage_count -= 1
    if c == '>':
        not_garbage = True
    if c == '{':
        level += 1 * not_garbage
        score += level * not_garbage
    if c == '}':
        level += (-1 * not_garbage)
    garbage_count += not not_garbage
    i += 1

print(score, garbage_count)
