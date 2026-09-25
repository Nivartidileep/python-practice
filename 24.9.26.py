'''
#scope of the varibles -> scope is basically the region or area where  the data is accessible

#local scope,global scope, global keyword , enclosing scope (non local keyword) built-in scope

#local scope (local variables) --> variable(S) defind inside the function are accessible only
def data():
    """local scope"""
    name ="codegnan"
    return f'{name} is in vizag.'
print(data())
#print(name)  #raises NameError


#Global scope -----> variables defined outside the functions can be accessible inside the function also

count = 10 # global variable
def details():
    """Global scope"""
    print(f'value of count is {count} inside the function')
    count = count+5 #raises UnboundLocalError
details()
print(f'value of count is {count} outside the function')

# priority of local vs global
count = 10 # global varible
def details():
    """priority of local vs global"""
    count = 15 # local varible
    print(f'value of count is {count} inside the function')
    count = count+5
details()
print(f'value of count is {count} outside the function')

# usage of global keyword
count = 10 # global varible
def details():
    """usage of global keyword"""
    global count
    count = count+15
    print(f'value of count is {count} inside the function')
details()
print(f'value of count is {count} outside the function')


#Enclosing Scope --> Nested Functions

def outer():
    """Nested functions"""
    count = 5
    def inner():
        """Inner function to use count variable"""
        #print(count)
        nonlocal count
        count = count*4
        print(f'value of count is {count}')
    inner()
    print(f'value of count is {count} outside')
outer()


# built-in scope --> usage of built-in variables
len = 13
print(len)
print(type(len)) #now you are modifying
print(len*2)

#LEBG rule --->Local,enclosing,built-in ,global

#every buit_in datatype is a built in function --> int,float,str,list,tuple,set,dict.

print(bool('codegnan')) #returns boolean value (true)
print(float(int(bool(24))))#functions as first class objects

print(abs(-23)) #returns 23
'''









































