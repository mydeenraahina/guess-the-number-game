import random
def guess():
    y=random.randint(1,10)
    print("***guess the number!***")
    guess=int(input("Enter your guessed number:"))
    if guess==y:
        print('Congratulation you won in first try!!!')
    else:
        print('You have four more chance to won the game')
        guess1=int(input("Enter your guessed number:"))
        if guess1==y:
              print("Congratulation you won in second try!!")
        else:
            print('you have three more chance to win the game')
            guess2=input("enter your guessed number :")
            if guess2==y:
                print("Congratulation you won in third try!")
            else:
                print('You have two more chance to won the game')
                guess3=int(input("Enter your guessed number:"))
                if guess1==y:
                    print("Congratulation you won in fouth try...")
                else:
                    print('you have one more chance to win the game')
                    guess4=input("enter your guessed number :")
                    if guess4==y:
                        print("Congratulation you won in fifth try......")
                    else:
                        print('sorry better luck next time!')
name=input("Enter your name:")
print("welcome!",name,"our Number Guessing Game")
choice=input("Do you want to start this game :")#type yes to start/no to exit
if choice=="yes":
    guess()
else:
    print("type no to exit/yes to continue")
while True:
    a=input('enter your choice')#type yes to continue/no to exit
    if a=="yes":
        guess()
    else:
        print("--!--")
        break;
        

