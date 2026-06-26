import json

class Expense:
    def __init__(self, expense_name, expense_amount):
        self._expense_amount = expense_amount
        self._expense_name = expense_name

    @property
    def expense_amount(self):
        return self._expense_amount
    
    @expense_amount.setter
    def expense_amount(self, expense_amount):
        self._expense_amount = expense_amount

    @property
    def expense_name(self):
        return self._expense_name
    
    @expense_name.setter
    def expense_name(self, expense_name):
        self._expense_name = expense_name

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
    
    @property
    def user(self):
        return self._user
    
    @user.setter
    def user(self, user):
        self._user = user
    
    @property
    def expenses(self):
        return self._expenses
    
    @expenses.setter
    def expenses(self, expenses):
        self._expenses = expenses

class User:
    _id_counter = 0
    def __init__(self, user_name):
        self._user_name = user_name
        User._id_counter += 1
        self._user_id = f"{user_name}{User._id_counter}"
        self._expense_manager = Expense_Manager(self)
    
    @property
    def user_name(self):
        return self._user_name
    
    @user_name.setter
    def user_name(self, user_name):
        self._user_name = user_name

    @property
    def user_id(self):
        return self._user_id
    
    @user_id.setter
    def user_id(self, user_id):
        self._user_id = user_id

    @property
    def expense_manager(self):
        return self._expense_manager
    
    @expense_manager.setter
    def expense_manager(self, expense_manager):
        self._expense_manager = expense_manager
        


# def saving_to_file(user):
#     data = {
#         "user_name": user.user_name,
#         "user_id": user.user_id,
#         "expenses": [{"name": e.expense_name, "amount": e.expense_amount} for e in user.expense_manager.expenses]
#     }

#     with open(f"{user.user_id}.json", "w") as f:
#         json.dump(data, f)

# def load_from_file(user):
#     with open(f"{user.user_id}.json", "r") as f:
#         data = json.load(f)

#     user.user_name = data["user_name"]
#     user.user_id = data["user_id"]

#     user.expense_manager.expenses = [
#         Expense(e["name"], e["amount"])
#         for e in data["expenses"]
#     ]


# def save_user(user):
#     try:
#         with open("users.json", "r") as f:
#             users = json.load(f)
#     except FileNotFoundError:
#         users = []

#     users.append(user.user_id)

#     with open("users.json", "w") as f:
#         json.dump(users, f)

# def load_users():
#     try:
#         with open("users.json") as f:
#             return json.load(f)
#     except FileNotFoundError:
#         return []

def print_options():
    print("**********************")
    print("1. Create an account")
    print("2. Existing User")
    print("3. Close the application")
    print("**********************\n\n")

# main program

# users = load_users()

# valid_option = True
# while valid_option:
#     print_options()
#     option = int(input("Select the from above options (press: 1/2/3)"))
#     if option == 1:
#         user_name = input("Please enter the name" )
#         user = User(user_name)
#         save_user(user)
#         valid_option = False
#     elif option == 2:
#         attempt = 0
#         while(attempt < 3):
#             user_id = input("Please Enter your User ID: ")
#             attempt += 1
#             if user_id in users:
#                 valid_option = False
#                 break
#             else:
#               print("Invalid User ID!")
#     elif option == 3