import re
import string

def next_to_do(to_do, dependencies):
    # candidate to see if it has any dependencies
    candidate_index = 0
    while candidate_index < len(to_do):
        letter = to_do[candidate_index]
        # if this letter has dependencies, move on to the next
        if dependencies[letter]:
            candidate_index += 1
        # if no dependencies, then choose this letter
        else:
            return letter
    return None

# for a just-finished letter, remove the dependencies
def remove_dependencies(dependencies, finished):
    for letter in dependencies:
        if finished in dependencies[letter]:
            dependencies[letter].remove(finished)
    return dependencies

# completion durations for tasks are A:1, B:2, ... Z:26
durations = {letter: ord(letter) - 4 for letter in string.ascii_uppercase}
# regex to parse input
pre_post_pattern = re.compile(r'Step (?P<pre>[A-Z]) must be finished before step (?P<post>[A-Z]) can begin.')

dependencies = {letter: [] for letter in string.ascii_uppercase}
# read in dependencies
with open('input7.txt', 'r') as f:
    for line in f:
        match = re.match(pre_post_pattern, line)
        # if X depends on Y, we save X in a list of Y's dependencies
        dependencies[match.group('post')].append(match.group('pre'))

NUM_WORKERS = 5
workers = [None for x in range(NUM_WORKERS)]
# to start we have to complete A-Z
to_do = list(string.ascii_uppercase)
# will build up string of tasks completed
completed = ''
time = 0

# if there are remaining tasks to start or workers are still going, continue
while to_do or any(workers):
    # complete any tasks that have just finished
    for i in range(NUM_WORKERS):
        if workers[i]:
            workers[i]['remaining'] -= 1
            if workers[i]['remaining'] == 0:
                letter = workers[i]['letter']
                completed += letter
                dependencies = remove_dependencies(dependencies, letter)
                workers[i] = None
    # loop again to add tasks if possible to empty workers
    # done separately from previous loop as some might have just become available
    for i in range(NUM_WORKERS):
        if workers[i] is None:
            next_letter = next_to_do(to_do, dependencies)
            # next_letter can be None. If not, then do the task.
            if next_letter:
                workers[i] = {'letter' : next_letter, 'remaining' : durations[next_letter]}
                to_do.remove(next_letter)
    time += 1
# loop construction results in extra addition to `time`
print(time-1)