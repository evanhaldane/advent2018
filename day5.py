with open('input5.txt', 'r') as f:
    polymer = f.read()

i = 0


while i < len(polymer)-1:
    if polymer[i].swapcase() == polymer[i+1]:
        polymer = polymer[:i] + polymer[i+2:]
        i = max(0, i-1)
    else:
        i += 1

print(len(polymer))
