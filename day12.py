import re
import json
from pprint import pprint
from common import input

data = input(12).read()
nums = re.findall(r'-?\d+', data)
print(sum(map(int, nums)))

top = json.loads(data)

def sum_no_red(root):
    s = 0
    if isinstance(root, dict):
        for v in root.values():
            if v == 'red':
                return 0
            if isinstance(v, int):
                s += v
            elif isinstance(v, str):
                pass
            else:
                s += sum_no_red(v)
    else:
        for v in root:
            if isinstance(v, int):
                s += v
            elif isinstance(v, str):
                pass
            else:
                s += sum_no_red(v)
    return s

print(sum_no_red(top))
