from my_utils.iteration import transpose
from common import Input
import re

if __name__ == '__main__':

    t = [[101, 301, 501],
    [102, 302, 502],
    [103, 303, 503],
    [201, 401, 601],
    [202, 402, 602],
    [203, 403, 603]]



    tris = re.findall('\d+', Input(3).read())
    tris = [tris[s+offset:s+9:3] for s in range(0,len(tris),9) for offset in range(3)]
    tris = [sorted(map(lambda i: int(i), tri)) for tri in tris]
    possible = (sum(tri[:2]) > tri[2] for tri in tris)
    print(sum(possible))
