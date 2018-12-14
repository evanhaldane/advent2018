import re
from collections import defaultdict
with open('input4.csv', 'r') as f:
    stamps = [line for line in f]

# put stamps in chronological order
stamps.sort()
begin_shift_pattern = re.compile(r'\[\d+-(?P<month>\d+)-(?P<day>\d+) (?P<hour>\d+):(?P<minute>\d+)\] Guard #(?P<guard>\d+) begins shift')
falls_asleep_pattern = re.compile(r'\[\d+-(?P<month>\d+)-(?P<day>\d+) (?P<hour>\d+):(?P<minute>\d+)\] falls asleep')
wakes_up_pattern = re.compile(r'\[\d+-(?P<month>\d+)-(?P<day>\d+) (?P<hour>\d+):(?P<minute>\d+)\] wakes up')

# nested default dict for guards / minutes asleep
asleep_counts = defaultdict(lambda: defaultdict(int))

for stamp in stamps:
    match = re.match(begin_shift_pattern, stamp)
    if match:
        guard = int(match.group('guard'))
        continue
    match = re.match(falls_asleep_pattern, stamp)
    if match:
        sleep_minute = int(match.group('minute'))
        continue
    match = re.match(wakes_up_pattern, stamp)
    if match:
        wake_minute = int(match.group('minute'))
        # increase sleep counter for each minute asleep
        for minute in range(sleep_minute, wake_minute):
            asleep_counts[guard][minute] += 1

# find guard id that corresponds to most total minutes asleep
guard_with_most_sleep = max(asleep_counts.keys(), key=(lambda key: sum(asleep_counts[key].values())))
# for the above guard, find the minute on which they slept the most
most_sleepy_minute = max(asleep_counts[guard_with_most_sleep], key=(lambda key: asleep_counts[guard_with_most_sleep][key]))

# answer is product of above
guard_with_most_sleep * most_sleepy_minute

# find guard/minute that was the most frequent out of all possible guard/minutes
max_guard, max_minute = max([(guard, minute) for guard in asleep_counts for minute in asleep_counts[guard]], key = (lambda t: asleep_counts[t[0]][t[1]]))
# answer is the product of above
max_guard*max_minute