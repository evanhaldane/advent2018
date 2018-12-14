import string
import re

with open('input5.txt', 'r') as f:
    polymer = f.read()

# react all substrings and return length of result
def length_after_reacting(polymer):
    i = 0
    while i < len(polymer)-1:
        if polymer[i].swapcase() == polymer[i+1]:
            polymer = polymer[:i] + polymer[i+2:]
            i = max(0, i-1)
        else:
            i += 1

    return len(polymer)

resulting_lengths = {}

for char in string.ascii_lowercase:
    pattern = char +'|'+ char.swapcase()
    # remove all instances of that character, upper and lower
    stripped = re.sub(pattern, '', polymer)
    resulting_lengths[char] = length_after_reacting(stripped)

# print minimum resulting length
print(min(resulting_lengths.values()))