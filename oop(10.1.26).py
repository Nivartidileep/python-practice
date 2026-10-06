'''
OOP -> object oriented programing -> It is a principle or paradigm
which revolves around objects.

It ha two main concepts or object contains:
--> Attributes (data) --> properties or charactrics of an object
--> Methods (Behavior) --> it performs the actions.

Syntax:

Class ClassName:
   """Doc String"""
   def __init__(self,attrs):
   ......................
   .....................



   def method(self):
       statement(s)...
       ....................



Features:
# OOP ---> Encapsulation,Inhertance,Polymerorphisium,Abstration
#Encapulation: It is one of the key properties of OOP, which bundles
#the data including atributes and methods into a single class.
#It provides accessibility (public,private,protected)
#students class with basic details


class Students:
    """Students class with basic details"""
    #Attribute
    name = "Akash"
    age = 18
    location = "vizag"


    #Behavior(Actions)
    def details(self):
        print(f'{self.name} is {self.age) years old and is in {self.location}')
s1 = students()
print(dir(s1))
print(s1.age,s1.name,s1.location)
s1.details()
print(s1.__Class__) #returns class name (__class__)  --> dunder class
print(s1.__doc__) #returns doc string
#whatever objects we create its only same
s2 = students()
s2.name = "Dileep"
s2.location = "vizag"
s2.details()


# in the above case we want to modify  the attributes such that we can create
#Multiple  objects with specific attributed and methods

class Students:
    """ students class with  Actions"""
    def profile(self,name,age,email_id,mobile):
        self.name = name
        self.age = age
        self.email = email_id
        self.phone = mobile
    #To display the details
    def display(self):
        print(f'Student name is {self.name}')
        print(f'Student email id is {self.email} and age is {self.age}')
s1 = Students()
s1.profile("Akash",18,"akash123@gmail.com",8074432177)
s1.display()
print(s1.__dict__)
s2 = Students()
s2.profile("Dileep",22,"dileep2004@gmail.com",230098765)
s2.display()




#Now we will  take same above example and create constructor
class Students:
    """Students class with Actions"""
    def __init__(self,name,age,email_id,mobile):
        self.name = name
        self.age = age
        self.email = email_id
        self.phone = mobile
    #To display the details
    def display(self):
        print(f'Student name is {self.name}')
        print(f'Student email id is {self.email} and age is {self.age}')
s1 = Students("lokesh",24,"loki3004@gmail.com",34567898756)
s1.display()

print(s1.__dict__)
s2 = Students("Sandeep",21,"sandeep45@gmail.com",457890987645)
s2.display()
print(s2.__dict__)


'''
    

class cars:
    """cars class with Actions"""
    def __init__(self,brand,color,price):
        self.brand = brand
        self.color = color
        self.cost = price
        
    #To display the details
    def display(self):
        print(f'brand name is {self.brand}')
        print(f'car is {self.brand} and color in {self.color} cost of{self.cost}')
c1 = cars("BMW","white",167000)
c1.display()
print(c1.__dict__)



























































