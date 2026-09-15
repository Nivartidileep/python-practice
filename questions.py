'''
Input Formatting: Accept input from user
int,float,sring,comma seprated values,space seprated values


#Input from user --> input() --> can accept any type --> result -->str
name = input("enter the name:")
print(name)
print(type(name))
print(len(name))

#split()
#by default it will be sperated
names = input("enter the names:").split()
print(names)
print(type(names))
print(len(names))


#split(',') --> comma seprated values

names = input("enter the names:").split(',')
print(names)
print(type(names))
print(len(names))


#Accept single integer,multiple integer values, group of integers

num1 =  int(input("Enter the number:"))
print(num1)
print(len(num1))

#Every built-in datatype is a built-in functions --> Functions --> Objects

#Usage of map() --> group of integers

numbers = list(map(int,input("enter the values").split(',')))
print(numbers)
print(type(numbers))


#group of float values
tempratures = list(map(float,input("enter the values:").split(',')))
print(tempratures)
print(type(tempratures))
'''


#Accept multiple values --> integers,float,names(str)....
temprature,pressure = map(float,input("enter the values:").split(','))
print("temprature is",temprature)
print("pressure is ",pressure)






























