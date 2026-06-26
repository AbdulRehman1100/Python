
print("Calculate the factorial of a number")
print("**NOTE**:Factorial only exist for whole numbers by its definition\n")

print("Calculating factorial using a loop")
num = int(input("Enter a whole number: "))

num_copy = num
result = 1

# while(num_copy > 0):
#     result = result*num_copy
#     num_copy = num_copy - 1
# print(f"Factorial of {num} using loop is {result}\n")

def factorial(num):
    if(num < 2):
        return num
    else:
        result = num * factorial(num - 1)
        return result

print("Calculating by defining a recursive definition")
print(f"Factorial of {num} using its recursive definition is: {factorial(num)}")