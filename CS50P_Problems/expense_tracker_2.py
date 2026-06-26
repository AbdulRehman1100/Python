import sys

class Expense:
    def __init__(self, expense_name, expense_amount):
        self._expense_amount = expense_amount
        self._expense_name = expense_name

    # @property
    # def expense_amount(self):
    #     return self._expense_amount
    
    # @expense_amount.setter
    # def expense_amount(self, expense_amount):
    #     self._expense_amount = expense_amount

    # @property
    # def expense_name(self):
    #     return self._expense_name
    
    # @expense_name.setter
    # def expense_name(self, expense_name):
    #     self._expense_name = expense_name


class Expense_Manager:
    def __init__(self, user, expenses = None):
        self._user = user
        self._expenses = expenses if expenses is not None else []
    
    def add_expense(self, expense):
        self._expenses.append(expense)
    
    def remove_expense(self, expense):
        self._expenses.remove(expense)
    
    def calculate_total_expense(self):
        return sum(expense.expense_amount for expense in self.expenses)
    
    # @property
    # def user(self):
    #     return self._user
    
    # @user.setter
    # def user(self, user):
    #     self._user = user
    
    # @property
    # def expenses(self):
    #     return self._expenses
    
    # @expenses.setter
    # def expenses(self, expenses):
    #     self._expenses = expenses

class User:
    _id_counter = 0
    def __init__(self, user_name, user_id):
        self._user_name = user_name
        User._id_counter += 1
        self._user_id = user_id
        self._expense_manager = Expense_Manager(self)
    
    @property
    def user_name(self):
        return self._user_name
    
    @user_name.setter
    def user_name(self, user_name):
        self._user_name = user_name

    # @property
    # def user_id(self):
    #     return self._user_id
    
    # @user_id.setter
    # def user_id(self, user_id):
    #     self._user_id = user_id

    # @property
    # def expense_manager(self):
    #     return self._expense_manager
    
    # @expense_manager.setter
    # def expense_manager(self, expense_manager):
    #     self._expense_manager = expense_manager



def print_main_menu():
    print("**********************")
    print("1. Create an account")
    print("2. Existing User")
    print("3. Close the application")
    print("**********************\n\n")

def create_account():
   name = input("Enter your full name: ")
   user_id = input("Please username of your wish(must start with alphabet or underscore, only alphabet, number and underscore allowed) ")
   return User(name, user_id)

def exit_program():
     sys.exit(0)

def print_sub_menu():
    print("1. Add an expense")
    print("2. Delete an expense")
    print("3. Caculate total expenses")
    print("4. Print my expenses")


print_main_menu()

main_menu_choice = 1
while( 0 > main_menu_choice > 3):
    main_menu_choice = int(input("Select the from above options (press: 1/2/3)"))

match main_menu_choice:
    case 1:
        user = create_account()
    case 2:
        user_name = input("Enter your username: ")
        # later implemenetation
        # dummy user
        user = User("User", user_name)
    case 3:
        print("Thank you for choosing us")
        exit_program()

while True:
    print_sub_menu()

    sub_menu_choice = 1
    while( 0 > main_menu_choice > 5):
        sub_menu_choice = int(input("Select the from above options (press: 1/2/3/4/5)"))

    match sub_menu_choice:
        case 1:
            while
        case 2:
            pass
        case 3:
            pass
        case 4:
