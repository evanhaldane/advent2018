with open('input2.txt', 'r') as f:
    ids = [line for line in f]

for i in range(len(ids)):
    for j in range(i+1, len(ids)):
        id1 = ids[i]
        id2 = ids[j]
        differences = 0
        for char_index, character in enumerate(id1):
            if character != id2[char_index]:
                differences += 1
                if differences > 1:
                    break
        if differences == 1:
            print(id1)
            print(id2)

