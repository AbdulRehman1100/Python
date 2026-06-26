myfamily = {
    'child1' : {
        'name' : 'Sami Ullah',
        'age' : 43
    },
    'child2' : {
        'name' : 'Kaleem Ullah',
        'age' : 40
    },
    "child3" : {
    "name" : "Linus",
    "year" : 2011
    }
}

print(myfamily)

for x, obj in myfamily.items():
    print(x)

    for y in obj:
        print(y + ':', obj[y])