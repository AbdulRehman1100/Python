def is_prime(number):
    '''
    Return whether an integer is a prime number or not.
    '''
    if not isinstance(number, int):
        raise TypeError("number must be an integer")
    
    if number < 2:
        return False

    if number == 2:
        return True

    if number % 2 == 0:
        return False

    for i in range(3, int(number ** 0.5) + 1, 2):
        if number % i == 0:
            return False
    return True

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