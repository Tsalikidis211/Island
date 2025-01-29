# # # class Author:
# # #     def __init__(self, age=0):
# # #         self._age = age  # Initialize the private attribute _age
# # #         self.name = ""   # Initialize other attributes if needed
# # #         self.email = ""
# # #         self.gender = ""

# # #     def get_age(self):
# # #         return self._age

# # #     def set_age(self, x):
# # #         self._age = x

# # #     age = property(get_age, set_age)  # Create a property for age

# # # # Creating an Author instance
# # # martin = Author()

# # # # Setting the age using the setter
# # # martin.age = 105

# # # # Accessing the age using the getter
# # # print(martin.age)  # Output: 105
# # class Employee():
# #     def __init__(self, firstname,lastname,email):
       
# #        self.firstname=firstname
# #        self.lastname=lastname
# #        self.email=email
# #        self._workyears="30"

# #     def display(self):
# #         print(self.firstname)     
# #         print(self.lastname)
# #         print(self.email)
# #         print(self._workyears)
       
# # employeee = Employee("Guy","Laroche","paparopoulos@gmail.com")
# # employee2 =Employee("fds","fds","dfs@gmail.com")

# # print(employeee.firstname)     
# # print(employeee.lastname)
# # print(employeee.email)
# # print(employeee._workyears)

# f = open("tsalikidis1", "w")
# f.write("123456")
# f.close()

# f = open("tsalikidis1", "r")
# x = (f.read())
# print(x)
# f = open("tsalikidis2","w")
# f.write(x)
# print(x)
# f.close()

import os

# Function to register a new user
def register_user():
    print("You need to register to use the ATM.")
    username = input("Enter your username: ")
    password = input("Enter your password: ")

    # Save username and password to a file
    with open("MyATM.txt", "w") as f:
        f.write(f"{username}\n{password}")
    print("Registration successful!")

# Function to log in with an existing user
def login_user():
    print("You need to log in to access your ATM account.")
    username_input = input("Enter your username: ")
    password_input = input("Enter your password: ")

    # Read stored username and password from the file
    try:
        with open("MyATM.txt", "r") as f:
            stored_username, stored_password = f.read().splitlines()

        if username_input == stored_username and password_input == stored_password:
            print("Login successful!")
        else:
            print("Incorrect username or password.")
    except FileNotFoundError:
        print("No user found. Please register first.")

# Main ATM menu function
def atm_menu():
    print("Hi, customer! You need to register or login to use the ATM:")

    while True:
        a = input("(1). Register - (2). Login: ")

        if a == '1':  # Registration
            register_user()
        elif a == '2':  # Login
            login_user()
        else:
            print("Invalid option. Please try again.")
            continue

        break  # Exit after registration or login

# Run the ATM system
atm_menu()
