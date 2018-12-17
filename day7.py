import re
import string

pre_post_pattern = re.compile(r'Step (?P<pre>[A-Z]) must be finished before step (?P<post>[A-Z]) can begin.')

# output is (X, Y) which means X depends on Y
def parse(line):
    match = re.match(pre_post_pattern, line)
    return match.group('post'), match.group('pre')

with open('input7.txt', 'r') as f:
    parsed = [parse(line) for line in f]

# sort in order of tasks which have dependencies
parsed.sort()

# left to do
to_complete = list(string.ascii_uppercase)
# will build up string of tasks completed
completed = ''

# candidate we are checking to see if complete-able or if it has dependencies
candidate_index = 0

# loop while there are still tasks to complete
while to_complete:
    letter = to_complete[candidate_index]
    # assume we have found a viable option unless we find a blocker    
    chosen = True
    for combo in parsed:
        # the dependcies are ordered so if we are past the letter alphabetically we stop checking
        if combo[0] > letter:
            break
        # this means the desired task has a dependency so we move on to the next option
        if combo[0] == letter:
            chosen = False
            candidate_index += 1
            break
    # if we've found something, then do the task and remove the relevant dependencies
    if chosen:
        completed += letter
        parsed = filter(lambda t: t[1] != letter, parsed)
        to_complete = filter(lambda t: t != letter, to_complete)
        # go back to the beginning
        candidate_index = 0
        
print(completed)