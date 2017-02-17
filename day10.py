

def look_and_say(start='1'):
    while True:
        current = start[0]
        count = 0
        n = []
        for c in start:
            if c == current:
                count += 1
            else:
                n.append(str(count))
                n.append(str(current))
                current = c
                count = 1
        n.append(str(count))
        n.append(str(current))
        ans = ''.join(n)
        yield ans
        start = ans

l = look_and_say('1113222113')
for _ in range(50):
    c = next(l)
print(len(c))
