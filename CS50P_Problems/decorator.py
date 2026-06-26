
# def decorator_function(original_function):
#     def wrapper_function():
#         print(f"{wrapper_function.__name__} executed before {original_function.__name__}")
#         return original_function()
#     return wrapper_function

# def display():
#     print("Display ran")
# decorated_display = decorator_function(display)
# decorated_display()


# @decorator_function # display = decorator_function(display)
# def display():
#     print("Display ran")

# display()


def decorator_function(original_function):
    def wrapper_function(*args, **kwargs):
        print(f"{wrapper_function.__name__} executed before {original_function.__name__}")
        return original_function(*args, **kwargs)
    return wrapper_function

@decorator_function # display = decorator_function(display)
def display():
    print("Display ran")

@decorator_function
def display_info(name, age):
    print(f"display_info ran with two arguments {name=} {age=}")

display_info("John" ,25)
display()
