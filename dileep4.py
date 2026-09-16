'''
input() ---> input formating
print() -----> output formating

a,b = 5,5.5
print(a,b) #by default sep=' '
print(a,b,sep=',')
print(9,15,sep=':')
print('codeganan','python','vizag',sep='--->')
#end by default throws new line,we can modify it...
print(a,b,end=' ')
print("codegnan is in vizag",end='\t')
print("pfs6 and da6")
print("------>caluclator-------->")
a = int(input("enter the value1:"))
b = int(input("enter the value2:"))
print(a+b)
print(a-b)
print(a*b)
print(a/b)
#usage of %d,%f,%s
#print("usage of %"%(args))
price = 45.356;grade = 'A';stock = 15
print("price is %d"%price)
print("price is %f"%price)
print("stock is %d"%stock)
print("grade is %s"%grade)

print("price is %.f"%price)
print("price is %.1f"%price)

#Area of circle when radius is 3.5 cm, round off the area to 2 decimal values
#take pi value as 3.1416


pi = 3.1416
r = 3.5
area = (pi*(r**2))
print("Area of circle is %.2f"%area)



#New Style Formattig ---> fstring (most recommanded)
name = "Codeganan";Batch = "PFS6"
print(f'{Batch} is in {name}')
print(f"Dileep is in {name}")
#Control block statements
#conditional(if,

Syntax for conditional statements
if
    <condition>
    statement(s)............
    .........................
    ...........

elif <conditions>:
    statement(s)............
    ............
    ......

else:
    statement(s)........
    .......

#BMI Converter(Body Mass Index --->weigght,hight) (wight kgs,hight cms,meter)
#hight ---> feets -> 1 feet --> 12 inches --> 1 inch --> 2.54 cm
#1 feet --> 30.48 cm --> 0.3 m
#bmi = weight / ((hight)**2)

weight = int(input("Enter the weight in kgs:"))
hight = float(input("Enter the hight in meters:"))
name = input("Enter the name")
bmi = weight / ((height)**2)
#print(bmi)
#now lets divide into categories


<18.5 ---> underweight
>=18.5 - 24.9 --->Healty
>=25 - 29.9 ---> Overweight
>30 ---> Obesity

weight = int(input("Enter the weight in kgs:"))
height = float(input("Enter the hight in meters:"))
name = input("Enter the name")
if weight > 0 and height > 0:
        bmi = weight / ((height)**2)
        if bmi<18.5:
            print(f'BMI of {name} is {bmi} and you are underweight --> Eat well')
        elif bmi >=18.5 and bmi<= 24.9:
            print(f'BMI of {name} is {bmi} and you are Healty --> keep consistency')
        elif bmi>=25 and bmi<= 29.9:
            print(f'BMI of {name} is {bmi} and you are Overwight -->\
            start Exercising')
        elif bmi>30:
            print(f'{name} is in Obese Category and bmi is {bmi}')
else:
        print("Do enter only +ve values greater then 0")
        
        



































































