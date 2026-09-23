'''
variable length arguments (*Args),keyword variable length arguments (**kwargs)

variable length arguments : we can pass any number of arguments,but tha data
will be srored in a (tuple), but we use symbolically *args as representation

def new(*d):
    """Usage of variables length arguments"""
    print(d)
    print(type(d))
#new()#it returns empty tuple as didn't pass any args.
#new(11,22,345)
#new('codegnan','python',2345678)

details = [12345678,'pfs','sadfghjkl']
new(details)#In this case entire list is stored inside a tuple as a single
#obj
new(*details)#In this case we can extract from above list as
#a tuple

a,b,c  = 1,3,5
a,*b,c = 1,'dileep','asdfghjk','qwertyuio',55
print(a)
print(c)
print(b)




#* is mainly used to unpack the values from a collection
a = ['sdfghjk','qwertyu','zxcvbm',45,34.8]
print(*a)
for i in a:
    print(i,end= " ")
# In above case both for loop and line 32 result is same.
    

def add(*a):
    """Sum of arguments usage using *args"""
    print(a)
    print(type(a))
    result = 0
    for i in a:
        result = result +i
        #print(result)
    #return result  
#print(add())
#print(add(1,2,3))
print(add(12,3,4,'codegnan','dileep',2.3))


def add(*a):
    """Sum of arguments usage using *args"""
    print(a)
    print(type(a))
    result = 0
    for i in a:
        #if type(i) == int or type(i) == float:
        if type(i) in (int,float):
            result = result +i
            #print(result)
    return result
print(add())
print(add(1,3,4,'codegnan','saketh',2.3))


# keyword variable length arguments -->we can pass any no. of keyword
#arguments will have represented in dictnary.

def admission (**kwags):
    """Usage of keyword variable length arguments"""
    print(kwags)
    print(type(kwags))
#admission(name="Dileep",mobile=123456789,email_id='dileep@codegnan.com')
details ={'id_nos':[234,456,432],
          'names':['Akash','Dileep','Sunny'],
          'batchs':['DA','PFS','JFS']}
admission(**details)


def simple(*a,**b):
    """Usage of *args and **kwargs"""
    print(a)
    print(b)
    result = 0
    for i in a:
        if type(i) in (int,float):
            result = result +i
    print(result)
    for key,value in b.items():
        print(f'key is {key}')
        print(f'value is {value}')
simple()
simple(1,2,3,'poll',23,name = "Dileep",place="vizag")
simple(1234567,12345,234568,'doing',email='wertyu@gamil.com',batch ="cse")

>>>> Nxt class:scope of variables,bult in functions,annominaus....
        





       
