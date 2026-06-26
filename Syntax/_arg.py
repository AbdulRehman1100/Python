
# *args

# def my_function(*number):
#     if(len(number) == 0):
#         return None
#     max_num = number[0]
#     for num in number:
#         if num > max_num:
#             max_num = num
#     return max_num

# print(my_function())

# **kwargs

def my_function2(username, **details):
    print("Username : ", username)
    print("Additional detail:")
    for key, value in details.items():
        print(" ", key + ":", value)

my_function2("emol123", age = 25, city = "Oslo", hobby = "coding")