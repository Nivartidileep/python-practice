'''
Inheritence:
Usage of Inheritence:
1.make the property of code Reusablity.

#Banking Scenario ---> Single Inheritence

class RBI:
    """Base Class"""
    cash = 100000000 #class variable
    #classmethod
    @classmethod
    def available_cash(cls):
        print(f"available cash with RBI is {RBI.cash}")
        
u1 = RBI()
print(u1.cash)
u1.available_cash()
print(RBI.cash)
RBI.available_cash()
#
class SBI(RBI):
    """Derived class"""
    pass
u1=SBI()
u1.available_cash()

class HDFC(RBI):
    """Derived class-2"""
    cash=5000000 #class variable
    @classmethod
    def hdfc_cash(cls):
        print(f"HDFC Cash is {cls.class}")
        print(f"Total Cash is {cls.Cash+RBI.Cash}")
u1=HDFC()
print(u1.cash)
u1.available_cash()
u1.hdfc_cash()


#Task : Convert same to Hierarchical also make use of public private,
#along with classmethods,class variables usage.

#kid-father property scenario -->

class father:
    """father prop only interms in cash"""
    def __init__(self):
        self.property=5000000
    def father_prop(self):
        print(f"father property is{self.property}")
#class kid(father):
        #pass
class kid(father):
    """kid has started earning"""
    def __init__(self):
        self.property=250000
    def kid_prop(self):
        print(f"kid property is{self.property}")
        print(f"total property is{self.property+self.property}")
#obj=father()
#obj.father_prop()
obj=kid()
print(obj.property)
obj=father_prop()
obj=kid_prop()

#Constructor overriding can be avoided by usage of super().
calling superclass constructor with args --->
class father:
    """father property only interms in cash"""
    def __init__(self):
        self.fproperty=5000000
    def father_prop(self):
        print(f"father property is{self.property}")
class kid(father):
    """kid has started earning"""
    def __init__(self):
        super().__init__() #calling superclass constructor
        self.property=250000
    def kid_prop(self):
        print(f"kid property is{self.property}")
        print(f"total property is{self.property+self.property}")
obj1=kid()
obj1.father_prop()
obj1.kid_prop()


#calling superclass constr with arguments

class father:
    """father property only interms in cash"""
    def __init__(self,prop1):
        self.fproperty=prop1
    def father_prop(self):
        print(f"father property is {self.property}")
class kid(father):
    """kid has started earning"""
    def __init__(self,prop2,prop1):
        super().__init__(prop1) #calling superclass constructor with args
        self.property=prop2
    def kid_prop(self):
        print(f"kid property is {self.kproperty}")
        print(f"total property is {self.kproperty + self.fproperty}")
u1=kid(450000,2500000)
u1.father_prop()
u1.kid_prop()


#Method Overriding ==> When we define same method same in parent class and also child class
#we prefer ==> super().method()

class Square:
    """Base class"""
    def __init__(self,x):
        self.x = x
    def sarea(self):
        return self.x**2
class Rectangle(Square):
    """Derived class with constructor and method name same"""
    def __init__(self,y,x):
        super().__init__(x)#calling superclass constructor with args
        self.y = y
    def rarea(self):
        return f'Area of Rectangle is {self.x * self.y}'
a1 = Rectangle(8,7)
print(a1.rarea())
print(a1.sarea)


class Square:
    """Base class"""
    def __init__(self,x):
        self.x = x
    def area(self):
        return self.x**2
class Rectangle(Square):
    """Derived class with constructor and method name same"""
    def __init__(self,y,x):
        super().__init__(x)#calling superclass constructor with args
        self.y = y
    def area(self):
        super().area()
        print(f'Area of Rectangle is {self.x * self.y}')
x,y = map(int,input("Enter the values").split(','))
obj1 = Rectangle(y,x)
obj1.area()

'''
#method overriding will only happen with inhertence usage
'''
#parent (father,mother) --> child

class A:
    statement(s)....
    .....
class B:
    statement(s)....
    ....
class C(A,B):
    statement(s)....
    ......
'''


























































