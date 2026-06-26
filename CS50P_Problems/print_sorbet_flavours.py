FLAVORS = [
    "Banana",
    "Chocolate",
    "Lemon",
    "Pistachio",
    "Raspberry",
    "Strawberry",
    "Vanilla",
]

flavours_length = len(FLAVORS)

i = 0
while( i < flavours_length):
    j = i + 1
    while( j < flavours_length):
        print(f"{FLAVORS[i]}, {FLAVORS[j]}")
        j += 1
    i += 1

# pythonic way of doing this
# for i in range(len(FLAVORS)):
#     for j in range(i + 1, len(FLAVORS)):
#         print(f"{FLAVORS[i]}, {FLAVORS[j]}")

