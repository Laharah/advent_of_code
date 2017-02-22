from common import input

moves = input(1).read()
floor = 0
position = 0
for m in moves:
    position += 1
    if m == '(':
        floor += 1
    elif m == ')':
        floor -= 1
    if floor < 0:
        print("basement at positon ", position)
        break
print(floor)
