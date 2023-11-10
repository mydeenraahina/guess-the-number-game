import random
def main_block():
    computer_choice=random.randint(0,20)
    print("***guess the number!***")
    print(f"Guess a number between [0 to 20]")
    user_choice=int(input("Enter your guessed number:"))
    if user_choice==  computer_choice:
        print('Congratulation you won in first try!!!')
    else:
        print('You have four more chance to won the game')
        user_choice=int(input("Enter your guessed number:"))
        if user_choice==  computer_choice:
              print("Congratulation you won in second try!!")
        else:
            print('you have three more chance to win the game')
            user_choice=input("enter your guessed number :")
            if user_choice== computer_choice:
                print("Congratulation you won in third try!")
            else:
                print('You have two more chance to won the game')
                user_choice=int(input("Enter your guessed number:"))
                if user_choice == computer_choice:
                    print("Congratulation you won in fouth try...")
                else:
                    print('you have one more chance to win the game')
                    user_choice=input("enter your guessed number :")
                    if user_choice== computer_choice:
                        print("Congratulation you won in fifth try......")
                    else:
                        print('computer won the game!')
name=input("Enter your name:")
print("welcome!",name,"our Number Guessing Game")
choice=input(f"Do you want to start this game [yes/no]:")#type yes to start/no to exit
if choice=="yes":
    main_block()
    while True:
        a=input(f"Enter your choice[yes/no]")#type yes to continue/no to exit
        if a=="yes":
            main_block()
        else:
            print("--Exit!--")
            break
else:
    print("Exit!")

        
