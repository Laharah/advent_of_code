from my_utils.iteration import transpose
from common import Input
from collections import Counter

entries = (l.strip() for l in Input(6))
entries = transpose(entries)
message = []
print(''.join(Counter(c).most_common()[-1][0] for c in entries))
