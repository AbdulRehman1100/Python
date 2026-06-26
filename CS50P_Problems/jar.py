
class Jar:
    def __init__(self, capacity=12):
        if not isinstance(capacity, int) or capacity < 0:
            raise ValueError
        self._capacity = capacity
        self.no_of_cookies = 0

    def __str__(self):
        return "🍪" * self.no_of_cookies
    
    def deposit(self, n):
        if self.no_of_cookies + n <= self.capacity:
            self.no_of_cookies += n
        else:
            raise ValueError

    def withdraw(self, n):
        if self.no_of_cookies - n >= 0:
            self.no_of_cookies -= n
        else:
            raise ValueError

    @property
    def capacity(self):
        return self._capacity

    @property
    def size(self):
        return self.no_of_cookies
    
def main():
    jar = Jar()
    print("Number of cookies available to eat:", jar.size, "and Jar capacity:", jar.capacity)
    jar.deposit(int(input("Enter no. of cookies: ")))
    print("Number of cookies available to eat:", jar)
    jar.withdraw(int(input("widthdraw no. of cookies: ")))
    print("Number of cookies available to eat:", jar)

if __name__ == "__main__":
    main()