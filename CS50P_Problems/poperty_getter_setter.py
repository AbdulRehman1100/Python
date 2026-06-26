
# setter_getter using property decorator -- python feature


class Employee:

    raise_amount = 1.04
    no_of_emp = 0

    def __init__(self, first, last, age, pay):
        self.first = first
        self.last = last
        self.age = age
        self.pay = pay
        # self.email = first + "." + last + "@Company" 
        Employee.no_of_emp += 1
    
    @property
    def full_name(self):
        return '{} {}'.format(self.first, self.last)
    
    @property
    def email(self):
        return self.first + "." + self.last + "@Company"
    
    @full_name.setter
    def full_name(self, name):
        self.first, self.last = name.split(" ")

    @full_name.deleter
    def full_name(self):
        self.first = None
        self.last = None

    @property
    def get_pay(self):
        return self.pay
    
    @get_pay.setter
    def set_pay(self, pay):
        self.pay = pay


emp_1 = Employee("Abdul", "Rehman", 25, 50000)
emp_2 = Employee("Saif", "Ullah", 30, 60000,)


# emp_1.first = "Ali"
# print(emp_1.first)
# print(emp_1.email)
# print(emp_1.full_name)

# emp_1.full_name = "Rust Chole"
# print(emp_1.full_name)

# del emp_2.full_name
# print(emp_2.full_name)

print(emp_1.get_pay)
emp_1.set_pay = 10000
print(emp_1.get_pay)