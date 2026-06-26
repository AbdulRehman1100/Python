
# dunder method -- we can overload python bulit in functions and operators to work with our classes


class Employee:

    raise_amount = 1.04
    no_of_emp = 0

    def __init__(self, first, last, age, pay):
        self.first = first
        self.last = last
        self.age = age
        self.pay = pay
        self.email = first + "." + last + "@Company"
        Employee.no_of_emp += 1

    def full_name(self):
        return '{} {}'.format(self.first, self.last)
    
    def  apply_raise(self):
        self.pay = self.pay * self.raise_amount

    @classmethod #class method
    def set_raise_amount(cls, amount):
        cls.raise_amount = amount

    @classmethod #alternative constructor
    def from_str(cls, emp_str):
        first, last, age, pay = emp_str.split("-")
        return cls(first, last, age, pay)

    def __repr__(self):
        return f"Employee({self.first}, {self.last}, {self.age}, {self.pay})"
    
    def __str__(self):
        return f"Full Name: {self.first} - {self.last}, Email Address: {self.email}"
    
    def __len__(self):
        return (len(self.first) + len(self.last))


emp_1 = Employee("Abdul", "Rehman", 25, 50000)
emp_2 = Employee("Saif", "Ullah", 30, 60000,)
    
print(emp_1)
print(emp_1.__repr__())

print('\n')
print(len(emp_1))
