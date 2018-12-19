with open('input8.txt', 'r') as f:
    numbers = [int(x) for x in f.read().rstrip().split(' ')]

# stack of children / metadata
num_children = [numbers[0]]
num_metadatas = [numbers[1]]
# current position in list of numbers
cursor = 2
# found metadata numbers
metadatas = []

# keep looping while there are still children nodes to find
while num_children:
    # if no more on this level, then the next numbers are metadata
    if num_children[-1] == 0:
        metadatas.extend(numbers[cursor:cursor + num_metadatas[-1]])
        cursor += num_metadatas[-1]
        # remove the number of children / metadata from the stack
        num_children = num_children[:-1]
        num_metadatas = num_metadatas[:-1]
    else:
        # we will visit one child, so decrease
        num_children[-1] -= 1
        # this new child has its own number of children/metadata, so add to stack
        num_children.append(numbers[cursor])
        num_metadatas.append(numbers[cursor+1])
        cursor += 2

print(sum(metadatas))

    

