'''
Nested Loops ---> problems
Right Angled triangle pattern

*
**
***
****
*****

for i in range(5):
    for j in range(i+1): #5 or 1+1
        #print(f'i = {i}, j={j}')
        print('*',end=' ')
    print()
(inverted star)
*****
****
***
**
*

for i in range(5):
    for j in range(5-i): #5 or 1+1
       
        print('*',end=' ')
    print()

(star pyramid)

rows = 5
for i in range(1,rows+1):
    #print spaces
    for j in range(rows-i):
        print(" ",end='')
    #print stars
    for j in range(i):
        print('*',end=' ')
    print( )

floyd's triangle

1
2 3
4 5 6
7 8 9 10


num=1
for i in range(4):
    for j in range(i+1): 
       print(num,end=' ')
       num= num+1
    print()



A
B C
D E F
G H I J



0
1 1
2 2 2
3 3 3 3
4 4 4 4 4

for i in range(5):
    for j in range(i+1):
         print(i,end=' ')
    print()
        

A
B B
C C C
D D D D



tasks:

A
B B
C C C
D D D D

0
1 1
2 2 2
3 3 3 3
4 4 4 4 4

#Specialcase ----> Diamond pattern

-------------------------------------------------------
#DT,O,CB,EH,FH
#PROCUDURE ORIRNTED PROGRAMING -> FUNCTIONS -> A FUNCTION IS A BLOCK OF CODE THAT PERFORMS A SPECIFIC TASK

FUNCTIONS:


def intro():
    """Intro to Functions"""
    return "Hope i am learning the journey", "good"
print(intro())


#postional Arguments,
def add(a,b):
    """simple addition function"""
    return a+b
print(add(5,7)) #Addition
print(add('codegnan','python')) #concatenation
print(add([1,2,3],[8,9,89])) #Merging
c,d = map(int,input("Enter the values").split(','))
print(add(c,d))

#keyword arguments
def grocery(item,price):
    """keyword arguments usage"""
    print(f'item is {item}')
    print(f'price is {price}')
grocery("milk",35)
'''
#Default arguments
def grocery(item,price=50):
    """keyword arguments usage"""
    print(f'item is {item}')
    print(f'price is {price}')
grocery("milk",35)
grocery("Bread")


Next class:
1.**kwags**
2.*args*









