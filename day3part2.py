import re
from collections import defaultdict
claimed = defaultdict(list)

pattern = re.compile(r'#(\d+)+ @ (\d+),(\d+): (\d+)x(\d+)')
def parse(s):
    number, x_offset, y_offset, width, height = pattern.search(s).groups()
    return int(number), int(x_offset), int(y_offset), int(width), int(height)


with open('input3.txt', 'r') as f:
    lines = [line for line in f]

# mark all claims
for line in lines:
    number, x_offset, y_offset, width, height = parse(line)
    for x in range(x_offset + 1, x_offset + width + 1):
        for y in range(y_offset + 1, y_offset + height + 1):
            claimed[(x, y)].append(number)

# need to loop a second time as multiple claims come in unknown orders
for line in lines:
    number, x_offset, y_offset, width, height = parse(line)
    solo_claimed_squares = [claimed[(x,y)] for x in range(x_offset + 1, x_offset + width + 1) for y in range(y_offset + 1, y_offset + height + 1) if len(claimed[(x,y)]) == 1]
    if len(solo_claimed_squares) == width * height:
        print(number)

