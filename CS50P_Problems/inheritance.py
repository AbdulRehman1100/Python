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

class Developer(Employee):
   def __init__(self, first, last, age, pay, prog_lang):
       super().__init__(first, last, age, pay)
       self.prog_lang = prog_lang

class Manager(Employee):
    def __init__(self, first, last, age, pay, employees = None ):
        super().__init__(first, last, age, pay)
        if employees is None:
            self.employees = []
        else:
            self.employees = employees
    
    def add_emp(self, emp):
        self.employees.append(emp)

    def remove_emp(self, emp):
        if emp in self.employees:
            self.employees.remove(emp)
    
    def print_emps(self):
        for emp in self.employees:
            print("--> ", emp.full_name())

dev_1 = Developer("Abdul", "Rehman", 25, 50000, "C++")
dev_2 = Developer("Saif", "Ullah", 30, 60000, "Python")

# print(dev_1.prog_lang)
# print(dev_2.email)

# mang_1 = Manager("Sami", "Ullah", 40, 100000, [dev_1])
# # mang_1.print_emps()
# mang_1.add_emp(dev_2)
# # mang_1.print_emps()
# mang_1.remove_emp(dev_1)
# mang_1.print_emps()

