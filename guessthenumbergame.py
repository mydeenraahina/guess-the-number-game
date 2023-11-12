import random
def main_block():
    def number_guessing_game():
        rand_numbers=[i for i in range(0,21)]
        computer_choice=random.randint(0,20)
        print("Lets play....")
        print("***guess the number!***")
        print(f"Guess a number between [0 to 20]")
        try:
            while True:
                user_choice=int(input("Enter your guessed number:"))
                if user_choice in rand_numbers:
                    if user_choice==computer_choice:
                        print('Congratulation you won in first try!!!')
                    else:
                        print('You have four more chance to won the game')
                        break
                else:
                    print("Invalid number")
            while True:
                user_choice=int(input("Enter your guessed number:"))
                if user_choice in rand_numbers:
                    if user_choice==computer_choice:
                      print("Congratulation you won in second try!!")
                    else:
                        print('you have three more chance to win the game')
                        break
                else:
                    print("Invalid number")
            while True:
                user_choice=input("enter your guessed number :")
                if user_choice in rand_numbers:
                    if user_choice==computer_choice:
                        print("Congratulation you won in third try!")
                    else:
                        print('You have two more chance to won the game')
                        break
                else:
                    print("Invalid number")
            while True:
                user_choice=int(input("Enter your guessed number:"))
                if user_choice in rand_numbers:
                        if user_choice==computer_choice:
                            print("Congratulation you won in fouth try...")
                        else:
                            print('you have one more chance to win the game')
                            break
                else:
                    print("Invalid number")
            while True:
                user_choice=input("enter your guessed number :")
                if user_choice in rand_numbers:
                    if user_choice== computer_choice:
                        print("Congratulation you won in fifth try......")
                    else:
                        print('computer won the game!')
                        break
                else:
                    print("Invalid number")
        except ValueError:
            print("invalid value typed\ngame ternminated")
    choice=input(f"Do you want to start this game [yes/no]:")#type yes to start/no to exit
    if choice.lower()=="yes":
        number_guessing_game()
    elif choice.lower()=="no":
        print("exit")
    else:
        while True:
            print("type proper reply for request")
            choice=input(f"Do you want to start this game [yes/no]:")#type yes to start/no to exit
            if choice.lower()=="yes":
                number_guessing_game()
            elif choice.lower()=="no":
                print("exit")
                break
            else:
                print("Try again!!")
getting_name=input("Enter your name:")
print("welcome!",getting_name,"our Number Guessing Game")
main_block()
    
