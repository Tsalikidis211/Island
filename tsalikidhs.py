# # class Author:
# #     def __init__(self, age=0):
# #         self._age = age  # Initialize the private attribute _age
# #         self.name = ""   # Initialize other attributes if needed
# #         self.email = ""
# #         self.gender = ""

# #     def get_age(self):
# #         return self._age

# #     def set_age(self, x):
# #         self._age = x

# #     age = property(get_age, set_age)  # Create a property for age

# # # Creating an Author instance
# # martin = Author()

# # # Setting the age using the setter
# # martin.age = 105

# # # Accessing the age using the getter
# # print(martin.age)  # Output: 105
# class Employee():
#     def __init__(self, firstname,lastname,email):
       
#        self.firstname=firstname
#        self.lastname=lastname
#        self.email=email
#        self._workyears="30"

#     def display(self):
#         print(self.firstname)     
#         print(self.lastname)
#         print(self.email)
#         print(self._workyears)
       
# employeee = Employee("Guy","Laroche","paparopoulos@gmail.com")
# employee2 =Employee("fds","fds","dfs@gmail.com")

# print(employeee.firstname)     
# print(employeee.lastname)
# print(employeee.email)
# print(employeee._workyears)

f = open("tsalikidis1", "w")
f.write("123456")
f.close()

f = open("tsalikidis1", "r")
x = (f.read())
print(x)
f = open("tsalikidis2","w")
f.write(x)
print(x)
f.close()



    
       