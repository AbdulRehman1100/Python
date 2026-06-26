
list1 = [100, 50, 65, 82, 23]

def myfunc(n):
    return abs(n - 50)

list1.sort(key = myfunc)

print(list1)