list1 = ['apple', 'banana', 'mango', 'am', 'i']
list2 = []

# creating new list from existing list using for loop

for x in list1:
    if 'a' in x:
        list2.append(x)
print(list2)

# same thing using list comprehension

list3 = [x for x in list1 if 'a' in x]
print(list3)