'''
Email Automation using python ----> first we need turn on 2-mail
#create app password
smtplib ---> simple mail transfer protocal

import smtplib
#first connect gmail server
server = smtplib.SMTP('smtp.gmail.com',587)
print(server)
#start connection
server.starttls()
server.login('nivarthiusha936@gmail.com','uabm kcnr vwvm ureo') #give app password
#give your desired message
message = "hello Guys......Hope i am doing well...."
server.sendmail("nivarthiusha936@gmail.com",
                "nivarthiusha936@gmail.com",message)
server.quit()
print("Mail Sent....")

#Now we will add subject
import email
import smtplib
#MIME ---> Multipurpose mail extension
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
msg = MIMEMultipart()
print(msg)
#now add from, to, subject
From = "nivarthiusha936@gmail.com"
To = "nivarthiusha936@gmail.com"
Subject = "Email Automation using python"
msg['From'] = From
msg['To'] = To
msg['Subject'] = Subject
body = "Prepare well and make sure to present well"
msg.attach(MIMEText(body))
#finally convert above as string
text = msg.as_string()
server = smtplib.SMTP('smtp.gmail.com',587)
#start connection
server.starttls()
server.login('nivarthiusha936@gmail.com','uabm kcnr vwvm ureo') #give app password
server.sendmail(From,To,text)
server.quit()
print("Mail Sent....")

#now extend this we can also send otp to users
import email
import smtplib
#MIME ---> Multipurpose mail extension
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import math,random

#as we want to generate random number
digits = "0123456789"
OTP = ""
#Now we will create OTP using  math and random
for i in range(4):
    OTP += digits[math.floor(random.random()*10)]
#print(OTP)
msg = MIMEMultipart()
body = f'your OTP is {OTP}'
From = "nivarthiusha936@gmail.com"
To = "nivarthiusha936@gmail.com"
Subject = "You have recived an Order"
msg['From'] = From
msg['To'] = To
msg['Subject'] = Subject
msg.attach(MIMEText(body))
#finally convert above as string
text = msg.as_string()
server = smtplib.SMTP('smtp.gmail.com',587)
#start connection
server.starttls()
server.login('nivarthiusha936@gmail.com','uabm kcnr vwvm ureo') #give app password
server.sendmail(From,To,text)
user = input("Enter the OTP")
if user == OTP:
    print("Authorization succuss")
else:
    print("Check the OTP again")
    

# attachment

import email
import smtplib
#MIME ---> Multipurpose mail extension
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
#Now to add attachment
from email.mime.base import MIMEBase #to addup our attachment
from email import encoders
import os

#Now let us add attachment
attach = "Nivarti Dileep.pdf" #attachment
msg  = MIMEMultipart()
#now add from,to,subject
From = "nivarthiusha936@gmail.com"
To = "nivarthiusha936@gmail.com"
Subject = "Email Automation using python"
msg['From'] = From
msg['To'] = To
msg['Subject'] = Subject
body = "Prepare well and make sure to present well"
#we will be using MIMEBase and Encoders to use the attachment
msg.attach(MIMEText(body))
part = MIMEBase('application','octet-stream')
part.set_payload(open(attach,'rb').read())
#now we will use encoders to encode the file
encoders.encode_base64(part)
#now to add the header the file
part.add_header('content-Disposition',
                'attachment ;filename="%s" '
                %(os.path.basename(attach)))
msg.attach(part)
text = msg.as_string()
server = smtplib.SMTP('smtp.gmail.com',587)
server.starttls()
server.login(From,'uabm kcnr vwvm ureo')
server.sendmail(From,To,text)
server.quit()
print("Mail sent")


'''


def solve():
    name = input().strip()
    otp = input().strip()
    subject = "Subject: Login Verification"
    body = "Hello " + name + ", your OTP is " + otp + "."
    print(subject)
    print(body)

if __name__ == "__main__":
    solve()






















