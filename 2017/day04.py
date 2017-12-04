from common import Input

total = 0
for line in Input(4):
    words = set()
    for word in (''.join(sorted(c for c in w)) for w in line.strip().split()):
        if word in words:
            break
        words.add(word)
    else:
        total += 1
print(total)
