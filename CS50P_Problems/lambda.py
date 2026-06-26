
# def my_func(n):
#     return lambda a : a * n

# mydoubler = my_func(2)
# mytripler = my_func(3)

# print(mydoubler(11))
# print(mytripler(11))


def transform(*arg, transform_function):
    return [transform_function(x) for x in arg]

print(transform(3, lambda a : a * 2))