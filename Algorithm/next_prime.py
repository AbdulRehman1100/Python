from is_prime import is_prime

def next_prime(number):
    '''Return next prime number for the given number'''
    if not isinstance(number, int):
        raise TypeError

    if number < 2:
        return 2

    # increment number to its immediate next odd number
    if number % 2 == 0:
        number += 1
    else:
        number += 2

    while not is_prime(number):
        number += 2
    return number