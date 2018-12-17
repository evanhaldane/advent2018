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

areas = {i: 0 for i in range(len(coordinates))}
for x in range(min_x-1, max_x+2):
    for y in range(min_y-1, max_y+2):
        distances = map(lambda t: abs(t[0] - x) + abs(t[1] - y), coordinates)
        shortest = min(distances)
        closest_point_index = filter(lambda i: distances[i] == shortest, range(len(distances)))
        if len(closest_point_index) > 1:
            continue
        i = closest_point_index[0]
        if x == min_x - 1 or x == max_x + 1 or y == min_y - 1 or y == max_y + 1:
            areas[i] = 'infinite'
            continue
        if areas[i] != 'infinite':
            areas[i] += 1

print(max([areas[i] for i in areas if areas[i] != 'infinite']))