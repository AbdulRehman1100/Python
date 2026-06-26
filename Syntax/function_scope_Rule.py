
# LEGB

x = "global"

def outer():
    x = "enclosing"
    print("Outer:", x)
    def inner():
        x = "local"
        print("Inner: ", x)
    inner()

outer()

print("Global:", x)