
#Compute x**n using loops

print("Calculate base number by th specified power using a loop\n")
x = float(input("Enter the base number (real number): "))
n = int(input("Enter the the whole number to it should be raised to: "))

org_n = n

result = 1
while(n > 0):
    result = result*x
    n = n-1
print(f"The answer (using the loop) is: {result}")

print("\nConfirmed the result using the built-in formula for exponenation")
print(f"{x} raised to power {org_n} is {x**org_n}")