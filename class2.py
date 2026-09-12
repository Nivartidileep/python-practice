'''batch=['sai', 'pfs6', 'da6', 'dileep', 'loki', 'python', 'suma']
batch.insert(2,("vizag","hyd","vijayawada"))
#print(batch)
#print(len(batch))
#as we have a tuple inside a list
#print(len(batch[2]))
#print(len(batch[2]))
#print(batch[2][:21])#
#print(batch[2][1])#this returns 'hyd' --> string
#print(batch[2][::2])# retuns ("vizag","vijayawada")
print(batch[2].index('hyd'))
#index--> first occurance
#count--> retuns the count of objects
print(batch[2].count('codegnan'))#returns count as 0
#index will raise error,where as count will return 0
batch.insert(3,['pfs','da','jfs'])
print(batch)
print(batch[3][1])
# to convert only jfs upper case --> JFS
batch[3][2] = batch [3][2].upper()
print(batch[3][2])
#now we want to add new course in batch[3] position --> AAA
batch[3].append('AAA')
print(batch[3])
print(len(batch))
print(batch)
batch.remove('loki')
print(batch)
#remove --> value,pop --> index
batch.pop()#pop by default removes last index value
print(batch)
#batch[2].remove('hyd')#raises AtributeError
#del batch[2][1] #tuple is immutanle so we cant insert/remove
#we want to remove entire data but keep the list as is is --> clear()
batch.clear()
print(batch)
'''

#Leets work on Dictionaries
#dict --> {k:v}, keys must be unique
#keys can be int,float,string,list
details ={}
print(len(batch))
details['batch']=['pfs6']
print(batch)
details['course']=['python']
#print(len(batch))
#print(details)
details['student'] = ['sai','hema']
#we want to update the dict
details.update({'branch':('hyd','vizag'),
                'subjects':{'python','aptitude','softskills'}})
print(details)
print(len(details))
#first always check the type --> dict --> keys()
#keys(),values(),items()
#print(details.keys())#returns only keys
#print(details['batch'])
details['batch'].extend(['jfs','da'])
#print(details)
details['students'].extend(['anil','sana','akash'])
print(details)#here key should be checked
details['subjects'].add('dsa')#set is unique and unorderd
print(details)

#Task --> Details --> List,set,Dictionary (use codegnan portal as example)
#Exams,Mock Interviews,Project Demos

#push to Github --> share your link in whattsapp group















































