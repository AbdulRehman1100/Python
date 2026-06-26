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

emp_1 = Employee("Abdul", "Rehman", 25, 50000)
emp_2 = Employee("Saif", "Ullah", 30, 60000)

# print(emp_1)
# print(emp_2)


# print(emp_1.full_name())
# print(Employee.full_name(emp_1))

# print(Employee.raise_amount)
# print(emp_1.raise_amount)
# print(emp_2.raise_amount)

# emp_1.raise_amount = 1.05

# print("\n")
# print(Employee.raise_amount)
# print(emp_1.raise_amount)
# print(emp_2.raise_amount)

# print("\n")
# print(Employee.__dict__)
# print("\n")
# print(emp_1.__dict__)


# print(Employee.no_of_emp)
# print(emp_1.no_of_emp)

#class method
# Employee.set_raise_amount(1.06)
# print(Employee.raise_amount)

# altenative constructor

emp_3_str = "Waseem-Ullah-32-70000"
emp_4_str = "Habib-Ullah-35-80000"

# first, last, age, pay = emp_3_str.split("-")
# print
# emp_3 = Employee(first, last, age, pay)
# print(emp_3.full_name())


emp_3 = Employee.from_str(emp_3_str)
print(emp_3.full_name())