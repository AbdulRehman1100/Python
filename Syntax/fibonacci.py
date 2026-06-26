#Print nth fibonacci number in the terminal
print("This program will take a number from the user on the terminal and\n"
"print crossponding fibonacci number")

n = int(input("Please enter a number : "))

# print("\nCalculating using recursion")

# def fib(n):
#     if(n == 0):
#         return 0
#     elif(n == 1):
#         return 1
#     else:
#         return fib(n - 1) + fib(n - 2)
    
# print(f"The {n}th fibonacci number is: {fib(n)}")

# print("\nCalculating using loop")

a = 0
b = 1
result = 0
n_copy = n
while (n > 0):
   result = b
   b = a + b
   a = result
   n = n-1

print(f"The {n_copy}th fibonacci number is: {result}")
        