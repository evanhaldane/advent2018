import re
claimed = {(i,j):0 for i in range(1,1001) for j in range(1,1001)}

pattern = re.compile(r'#\d+ @ (\d+),(\d+): (\d+)x(\d+)')
def parse(s):
    x_offset, y_offset, width, height = pattern.search(s).groups()
    return int(x_offset), int(y_offset), int(width), int(height)

with open('input3.txt', 'r') as f:
    for line in f:
        x_offset, y_offset, width, height = parse(line)
        for x in range(1, width+1):
            for y in range(1, height+1):
                claimed[(x_offset+x, y_offset+y)] += 1

print(sum([claimed[tup] > 1 for tup in claimed]))
