import re
from collections import defaultdict
with open('input4.csv', 'r') as f:
    stamps = [line for line in f]

# put stamps in chronological order
stamps.sort()
begin_shift_pattern = re.compile(r'\[\d+-(?P<month>\d+)-(?P<day>\d+) (?P<hour>\d+):(?P<minute>\d+)\] Guard #(?P<guard>\d+) begins shift')
falls_asleep_pattern = re.compile(r'\[\d+-(?P<month>\d+)-(?P<day>\d+) (?P<hour>\d+):(?P<minute>\d+)\] falls asleep')
wakes_up_pattern = re.compile(r'\[\d+-(?P<month>\d+)-(?P<day>\d+) (?P<hour>\d+):(?P<minute>\d+)\] wakes up')

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
        for minute in range(sleep_minute, wake_minute):
            asleep_counts[guard][minute] += 1

guard_with_most_sleep = max(asleep_counts.keys(), key=(lambda key: sum(asleep_counts[key].values())))
most_sleepy_minute = max(asleep_counts[guard_with_most_sleep], key=(lambda key: asleep_counts[guard_with_most_sleep][key]))
