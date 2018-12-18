from collections import defaultdict
seen = defaultdict(bool)

with open('input1.csv', 'r') as f:
    changes = [int(x) for x in f]

found_repeat = False
cumulative = 0
while not found_repeat:
    for change in changes:
        cumulative += change
        if cumulative in seen:
            found_repeat = True
            break
        else:
            seen[cumulative] = True

print(cumulative)