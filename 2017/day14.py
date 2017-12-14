from day10 import dense_hash
from my_utils.iteration import chunk, chain
from my_utils.graphs import neighbors4, dijkstra_all_paths

KEY = 'uugsqrei'

# KEY = 'flqrgnkx' # Test key


def knot_hash(s):
    'return a knot hash as a series of bytes'
    return bytes(int(''.join(x), 16) for x in chunk(dense_hash(s), 2))


def build_disk(key=KEY):
    'given a key, create the fragmented disk based on the knot hash of the lines'
    disk = []
    for i in range(128):
        b = knot_hash(key + '-{}'.format(i))
        s = ''.join('{:08b}'.format(x) for x in b)
        disk.append(list(int(x) for x in s))
    return disk


def build_image(disk):
    'convert the disk to a printable and non-int format'
    image = []
    for line in disk:
        image.append(['#' if x else '.' for x in line])
    return image


def region_fill(image):
    """
    convert a disk image to str(int) format, fill and number the contiguous regions.
        blank regions will be changed to '0'
    """
    region = 1

    def moves(point):
        for r, c in neighbors4(point):
            try:
                if image[r][c] == '#' and all(x >= 0 for x in (r, c)):
                    yield (r, c)
            except IndexError:
                continue

    for r in range(len(image)):
        for c, v in enumerate(image[r]):
            if v == '#':
                region_points = dijkstra_all_paths((r, c), moves).parents
                for y, x in region_points:
                    image[y][x] = str(region)
                region += 1
            elif v == '.':
                image[r][c] = '0'


def visualize(image):
    """
    visualize an image by making all blocks take up the same space and give regions a
    distinct symbol. Empty blocks will be spaces.
    """
    for line in image:
        print(''.join(chr(int(x) + 32) for x in line))


if __name__ == '__main__':
    disk = build_disk(KEY)
    image = build_image(disk)
    region_fill(image)
    visualize(image)

    print('Total blocks in use:', end=' ')
    print(sum(sum(line) for line in disk))

    print('Total Distinct Regions:', end=' ')
    print(max(int(x) for x in chain(*image)))
