
print("This program will return sum of numbers between two integer numbers given by the user")

a = int(input("Enter the first number: "))
b = int(input("Enter the second number: "))

sum = 0
for x in range(a, b + 1): #range add does include end number
    sum = sum + x

print(f"The sum of numbers between {a} and {b} including is {sum}")