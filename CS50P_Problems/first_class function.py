
def message(greeting):
    def inner_fun(name):
        print(f"{greeting}, {name}")
    return inner_fun

greet = message("Hello")

greet("Abdul Rehman")

# Closure kya hai yahan?
# inner_fun is the closure.
# A closure is a function that remembers variables from its enclosing scope even after that outer function has finished executing.
# Here, inner_fun remembers greeting — even after message() has returned.


# def custom_map(func, list):
#     result = []
#     for x in list:
#         result.append(func(x))
#     return result

# def square(n):
#     return n * n

# nums = [1, 2, 3, 4, 5]
# print(custom_map(square, nums))