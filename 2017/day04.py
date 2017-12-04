from common import Input

total = 0
for line in Input(4):
    words = set()
    for word in line.strip().split():
        sword = ''.join(sorted(word))
        if word in words or sword in words:
            break
        words.add(word)
        words.add(sword)
    else:
        total += 1
print(total)
