from hashlib import md5
from itertools import count

KEY = 'bgvyzdsv'

for i in count():
    d = md5(bytes(KEY + str(i), 'UTF8')).hexdigest()
    if d.startswith('000000'):
        print(i)
        print(d)
        break
