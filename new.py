
'''
a module is a python file (.py) containing usable logic
'''
import sept26
print(dir(sept26))# directory will return all avalible methods
print(type(sept26.data))
print(type(sept26.details))
# always first check the type



print(sept26.data)
print(sept26.details("codegnan","vizag"))
#in above cases we are accessing via modules name

from sept26 import data
print(data)

print(data.keys())

data['marks'] = [45,35,25,20]
print(data)

#print(details()) it raises errors as its not imported
print(sept26.__doc__) #it returns doc string(description)

from sept26 import *

print(data)
print(details('jhanavi','dileep'))
