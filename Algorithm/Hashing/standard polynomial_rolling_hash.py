# standard polynomial rolling hash
def polynomial_rolling_hash(string, base, mod=1000000007):
    result = 0
    power = 1
    for char in string:
        result = (result + ord(char) * power) % mod
        power = (power * base) % mod
    return result