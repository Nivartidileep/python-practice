'''
OOP ---> Encapsulation ---> key featues of OOP, it binds(bundled)
the data (attributes) and methods (actions) around a single class. It also provides
specific accessibilty as pubic, protected and private Attributes.

Lets understand in details about each one in detail

Public Attributes ---> These are defined inside the class and can be modified
outside the class


class Users:
    """Users data"""
    def __init__(self,name):
        self.name = name #Public attribute
    def details(self):
        print(f'user name is {self.name}')

u1 = Users("saketh")
u1.details()
print(u1.name)
u1.name = "Dileep"
u1.details()

#Protected Attribute : This is generally Preferred in devolper point of view, underscore before the attribute.
class Users:
    """Users data"""
    def __init__(self,name,_otp):
        self.name = name #Public attribute
        self._otp = _otp #Protected Attribute
    def details(self):
        print(f'user name is {self.name}')

u1 = Users("Saketh",8745)
print(u1._otp)
u1._otp = 3425
print(u1._otp)


Private Attribute: __ Leading underscores
# Python :  name Mangaling
class Users:
    """Users data"""
    def __init__(self,name,_otp,__password):
        self.name = name #Public attribute
        self._otp = _otp #Protected Attribute
        self.__password = __password
    def details(self):
        print(f'user name is {self.name}')

u1 = users("saketh",4523,"admin@123")
print(u1.name)
print(u1._otp)
#print(u1.__password)#it raises Attribute Errors 
print(u1._Users__password)#nameMangaling is used as we can access
#private attribute by classname with leading underscore usage....

#As NameMangling is not recommended approch we make use of Accessors and Modifiers in python.


class Users:
    """Users data"""
    def __init__(self,name,_otp,__password):
        self.name = name #Public attribute
        self._otp = _otp #Protected Attribute
        self.__password = __password #private Attribute
    #To make use of Private attri (getter method)
        def get_password(self):
            #return '******'
            return self.__password
    #Now to modify the password (setter method)
        def set_password(self,new_password):
            if len(new_password) >=6:
                self.__password = new_password
                print("password is Updated")
            else:
                print("Make sure to have password with min 6 Characters")
        def details(self):
            print(f'User name is {self.name}')

u1 = Users("saketh",5423,"admin")
print(u1.get_password())
u1.set_password("admin2")
print(u1.get_password())
print(u1.__dict__)
u2 = Users("sony",2345,"asdfgef")
print(u2.get_password())
u2.set_password("quer")
print(u2.get_password())
print(u2.__dict__)

#Task:
    #Use Geeter and Setter methods for both protected and private
    #attributes (take a new scenario),additionally u can also have
    #Public attribute


#Inheritence --> It is one of key featuresof OOP, which helps in (attribute, methods)
1.single Inheritence:
2.multiple
3.multilevel
4.hierarical

class Users:
    """Users details"""
    def __init__(self,fname,lname):
        self.fname = fname
        self.lname = lname

    def full_name(self):
        return self.fname + self.lname
#u1 = Users("dileep","nivarthi")
#print(u1.full_name())
class User_v2(Users):
    pass
u1 = User_v2(Users)
"""Updating username"""
def update_name(self):
        return self.fname.title().strip()+" "+self.lname.title().strip()
u1 = User_v2("dileep","  nivarthi")
print(u1.full_name())
print(u1.update_name())

'''

class BankAccount:

    def __init__(self, account_holder, account_number, balance, pin):
        # Public attribute
        self.account_holder = account_holder

        # Protected attribute
        self._account_number = account_number

        # Private attribute
        self.__balance = balance
        self.__pin = pin

    # Getter for protected attribute
    def get_account_number(self):
        return self._account_number

    # Setter for protected attribute
    def set_account_number(self, account_number):
        self._account_number = account_number

    # Getter for private balance
    def get_balance(self):
        return self.__balance

    # Setter for private balance
    def set_balance(self, balance):
        if balance >= 0:
            self.__balance = balance
        else:
            print("Balance cannot be negative")

    # Getter for private PIN
    def get_pin(self):
        return self.__pin

    # Setter for private PIN
    def set_pin(self, pin):
        if len(str(pin)) == 4:
            self.__pin = pin
        else:
            print("PIN must contain 4 digits")


# Creating object
account = BankAccount("Dileep", "ACC12345", 25000, 1234)

# Public attribute
print("Account Holder:", account.account_holder)

# Protected attribute using getter
print("Account Number:", account.get_account_number())

# Private attribute using getter
print("Balance:", account.get_balance())
print("PIN:", account.get_pin())

# Updating protected attribute using setter
account.set_account_number("ACC67890")

# Updating private attributes using setters
account.set_balance(30000)
account.set_pin(5678)

print("\nAfter Updating:")
print("Account Number:", account.get_account_number())
print("Balance:", account.get_balance())
print("PIN:", account.get_pin())




































































