
# printing every possible pairs of two letters, only lower case, one by line, ordered alphabetically.
a_to_z = [chr(x) for x in range(ord("a"), ord("z") + 1)]

for i in a_to_z:
    for j in a_to_z:
        print(i+j)


# distinct pairs
a_to_z = [chr(x) for x in range(ord("a"), ord("z") + 1)]

for i in a_to_z:
    for j in a_to_z:
        if i != j:
            print(i+j)