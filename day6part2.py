import csv
from collections import defaultdict

coordinates = []
with open('input6.csv', 'r') as f:
    reader = csv.reader(f, delimiter = ',')
    for row in reader:
        coordinates.append((int(row[0]), int(row[1])))

min_x = min([coordinate[0] for coordinate in coordinates])
max_x = max([coordinate[0] for coordinate in coordinates])
min_y = min([coordinate[1] for coordinate in coordinates])
max_y = max([coordinate[1] for coordinate in coordinates])

def manhattan_distance(t1, t2):
    return abs(t1[0] - t2[0]) + abs(t1[1] - t2[1])

def sum_distance((x,y)):
    return sum(map(lambda t: manhattan_distance(t, (x,y)), coordinates))

THRESHOLD = 10000
# probably (hopefully) the corners are going to be too far. if not, then flag and we'll adjust
count = 0
if (sum_distance((min_x, min_y)) < THRESHOLD or
    sum_distance((min_x, max_y)) < THRESHOLD or
    sum_distance((max_x, min_y)) < THRESHOLD or
    sum_distance((max_x, max_y)) < THRESHOLD):
    print("uh oh")

# okay we can start at corners (yay!)
for x in range(min_x, max_x + 1):
    for y in range(min_y, max_y + 1):
        total = sum_distance((x,y))
        if total < THRESHOLD:
            count += 1

print(count)