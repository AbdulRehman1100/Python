camel_case = input("camelCase: ")
snake_case = []



for c in camel_case:
    if c.isupper():
        snake_case.append("_")
        snake_case.append(c.lower())
    else:
        snake_case.append(c)

# snake_case = "".join("_" + c.lower() if c.isupper() else c for c in camel_case)

print("snake_case:", "".join(snake_case))
