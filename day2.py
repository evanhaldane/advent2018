from collections import defaultdict

def get_counts(s):
    count_dict = defaultdict(int)
    for char in s:
        count_dict[char] += 1
    return count_dict

twicers = 0
thricers = 0

with open('input2.txt', 'rb') as f:
    for line in f:
        counts = get_counts(line)
        is_twicer = 0
        is_thricer = 0
        for char in counts:
            if counts[char] == 2:
                is_twicer = 1
            if counts[char] == 3:
                is_thricer = 1
        twicers += is_twicer
        thricers += is_thricer

