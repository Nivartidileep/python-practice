'''import random
player1 = input("Enter any one number")
player2 = random.choice(['1 to 10'])
#print(player2)
if player1 == "1" and player2 == "2":
    print("player1 won")
elif player1 == "3" and player2 == "4":
    print("player2 won")
elif player1 == "5" and player2 == "6":
    print("player1 won")
elif player1 == "7" and player2 == "8":
    print("player2 won")
elif player1 == "9" and player2 == "10":
    print("player1 won")
elif player1 == player2:
    print("Its a Tie")
else:
    print("player2 won")
'''
import random
player1 = input("Enter any one number")
player2 = random.choice(['1 to 10'])
#print(player2)
if player1 == "1" and player2 == "5":
    print("player1 won")
elif player1 == "6" and player2 == "10":
    print("player2 won")
elif player1 == player2:
    print("Its a Tie")
else:
    print("player2 won")
