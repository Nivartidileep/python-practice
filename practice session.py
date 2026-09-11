
'''#1
student marks Analyzer
# for,while
## 3 steps in programming -> 1)input 2)output 3) logic
marks = []
for mark in range(3):
    mark = int(input("enter the marks:"))
    marks.append(mark)
marks.insert(0,90)
marks.extend([75,85])
#print(marks)
#remove()
if 75 in marks:
    marks.remove(75)
#removed value
print(marks.pop())
#print(marks)
# display final list and its length using len().
print("final list is",marks)
print("length of the list is",len(marks))


#2
numbers = [20, 10, 30, 20, 40, 20]
print("sorted list is")
numbers.sort()
print("reverse list is")
numbers.reverse()
if number in numbers:
  print("count is",numbers.count(number))
  print("first index is",numbers.index(number))
else:
    print("number is not found")
print("smallest value",numbers.min())
print("largest value",numbers.max())



#3

numbers = [10, 15, 20, 25, 30, 35]
even=[]
odd=[]
for number in numbers:
    if number % 2 == 0:
       even.append(number)
    else:
       odd.append(number)
print(even)
print(odd)
backup=numbers.copy()
numbers.clear()
print("original list:",numbers)
print("backup list:",backup)

#4
names = ["Asha", "Rahul", "Asha", "John", "Rahul"]
names=set(names)

names.add('meera')

names.update(['arun','priya'])

names.remove("John")

for name in names:
    names=list(names)
print(names)


#5

python_students = {"Asha", "Rahul", "John", "Meera"} 
da_students = {"Rahul", "Meera", "Arun"}
students=python_students|da_students
students=python_students & da_students
students=python_students - da_students
students=python_students ^ da_students
students=python_students.issubset(da_students)
students=python_students.issuperset(da_students)
students=python_students.isdisjoint(da_students)
print(students)




print("Hello guys Good Morning")
       
#perform operation as below
a=15
b=25
print(a+b)
'''
#Tokens --> keywords,variables,operators,punctuators [],(),{}

batch = ['pfs6','da6']
print(batch)
print(type(batch)) # everything is an object(pop--oop)
#len()--> returns the number of items in a collection

#print(len(batch))
batch.append('dileep')
#print(batch)
batch.extend(['loki','suma'])
#print(len(batch))
print(batch)
batch.insert(0,'sai')# inserts given value at specific index
#print(batch)
batch.insert(-1,'python')#value before index
print(batch)
print(len(batch))

#indexing --> [] --> index starts at 0 and ends at len(obj)-1
#also in revsere manner it is -1 to len(obj)

print(batch[0])
print(batch[4])
#print(batch[34])#index error --> length is only 7 we are accesing extra

#sclicing --> group of values[start:end] # start is included , end excluded
print(batch[0:3])
print(batch[4:6])
print(batch[2:4])
#last 3 elements --> we prefer negitive index
print(batch[-3:])
# first 3 elements
print(batch[:-3])
#sliding (start:end:step]
print(batch[::2])# it skips 1 element from start
print(batch[::3])# it skips 2 element from start
print(batch[::4])# it skips 3 element from start
print(batch[1:5:2])#first perform batch[1:5] --> then skip 1 element
#tryout
print(batch[:7:4])
print(batch[7::4])
print(batch[1::5])
print(batch[1:7:-2])
print(batch[-1:-4:-1])




























    
