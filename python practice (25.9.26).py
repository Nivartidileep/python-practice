'''arguments
==========
user defined functions,built in functions,anonumus function,variable keyword,recursive function.
anonimus function: nameless function (helper function) we define then by using lambda function.
syntax: lambda:arguments : expression
# area of rectangle where leangth and breadth are 7,4
def rectangle (l,b):
    """area of rectangle"""
    return l*b
print(rectangle(7,4))
print(type(rectangle))

#1 same using anonimus function.
area = lambda l,b : l*b
print(area(7,4))
print(type(area))

#ex: area of square with side value as 5.
def square (s):
    """side of a square"""
    return s**2
print(square(5))

#2 same using ananonimus function.
side = lambda s : s**2
print(side(5))
print(type(side))

## social media user login user first name , last name --> full name

#fname,lname = input('enter the names').split(',')
#print(fname,lname)
full_name = lambda fname,lname : fname.title().strip()+" "+lname>title().strip()
print(full_name(fname,lname))
#accepting input from user and find even or odd
n=int(input("enter a number:"))
result = lambda n : "even" if n%2 == 0 else "odd"
result1 = lambda n : n**2 if n%2 == 0 else n**3
print(result(n))
print("new result is ",result1(n))

#3 names =['codegnan','python','saketh','data','java']
g = lambda x :x in names
h = lambda x :len(x)in names
o = lambda x : len(x)
print(g('python'))
print(h('codegnan')
print(o('saketh'))

#filter(),map(),reduce()
#filter() --> we want to specific filtered result
data = [1,3,4,5,24,12,36,3]
#filter only even numbers from list
new_data = list(filter(lambda x:x%2==0,data))
print(new_data)

#Try above using user defined function with a for loop..

def final(data):
    """filter values"""
    new_data = []
    for i in data:
        if i % 2 == 0:
            new_data.append(i)
    return new_data
print(final(data))
#filter desired names from the list
names = ['saketh','python','akash','neha','sameer']
new_names = list(filter(lambda i:len(i) >=6,names))
print(new_names)
#map() --> it will apply logic for each value (google maps)
lst =  list(map(int,input("enter the values").split(',')))
print(lst)
data = [1,3,5,7,-23]
print(data)
final = list(map(lambda x,y:x+y,lst,data))
print(final)
#
prices = [2000,2500,1500,4500,3000]
#discount of 10% for every price
disc_price = list(map(lambda price:(price-price*0.1),prices))
print(disc_price)
#reduce --> functools
# reduce --> it will check for logic and make it to a single value
import functools
from functools import reduce
resullt = reduce(lambda x,y:x*y,[12,3,4,5,6])
print(result)
f = reduce(lambda x,y:x+y,[12,3,4,5,6])
print(f)
#recursive function
def test():
    """testing"""
    return test
print(test())
# let's link above case to factorial
#5! --> 5 *(5-1) * (5-2) * (5-3) * (5-4) * 1
'''
n = int(input("enter the values:"))
def fact(n):
    """factorial"""
    if n == 0 or n == 1:
        return 1
    elif n<0:
        return "input must be greater than 1"
    else:
        return n* fact(n-1)
print(fact(n))




