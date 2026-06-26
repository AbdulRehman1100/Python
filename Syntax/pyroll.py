
def pyroll(person, basic):
    house_rent = .45 * basic
    utilities = .10 * basic
    gross_salary = basic + house_rent + utilities
    tax = 0.15 * gross_salary
    net_salary = gross_salary - tax
    print(person, "\tGross Salary = ", gross_salary, "\tTax = ", tax, "\tNet Salary = ", net_salary, '\n')

for i in range(1, 5):
    person = "Person" + str(i)
    basic_salary = i * 30000
    pyroll(person, basic_salary)