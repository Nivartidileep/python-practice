'''#play a game
import random
player1 = input("Enter any one of the below:Rock,Paper,Scissors").lower()
player2 = random.choice(['Rock','Paper','Scissors']).lower()
print(player2)
if player1 == "rock" and player2 == "paper":
    print("player2 won")
elif player1 == "paper" and player2 == "scissors":
    print("player2 won")
elif player1 == "rock" and player2 == "paper":
    print("player2 won")
elif player1 == "scissors" and player2 == "rock":
    print("player2 won")
elif player1 == player2:
    print("Its a Tie")
else:
    print("player1 won")
    
----------------------------------------------------------------------------------------
'''
#QRCode --> pip install PyQRCode
import pyqrcode
import png
link =  "https://www.linkedin.com/in/dileep-nivarti-697599269/"
#now we create QR code for above link
qr = pyqrcode.create(link)
#print(qr)
#now we need to create an image for our code
#pip install pypng
qr.png("myqr.png",scale = 10)
'''
-----------------------------------------------------------------------------------------------

#Your task is make your VirtualAssistant
#play RPS game
#play Number Game  ---> [1,10]
#play your fav vedieo song
#create a qr code
#open your desired file in your system
---------------------------------------------------------------------------------------------------


'''
