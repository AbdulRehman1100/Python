def myfun(animal, name):
    print("I have a", animal)
    print("My", animal + '\'s name is', name)

myfun(name = 'Buddy', animal = 'Dog')

def my_function(a, b, /, *, c, d,):
    return a + b + c + d

print(my_function( 5, 10, d = 15, c = 30))