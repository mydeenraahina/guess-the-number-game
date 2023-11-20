<div align='center'>

<h1>THIS IS A NUMBER GUESSING GAME USING PYTHON</h1>
<p>This code is a number guessing game where the user has multiple chances to guess a randomly chosen number between 0 and 20.
  Here's a  working pattern of this code:
  User Name Input:

The program starts by asking the user to enter their name.

getting_name = input("Enter your name:")
Welcome Message and Game Initialization:

After obtaining the user's name, the program prints a welcome message.
The main_block function is then called to initiate the game.

print("Welcome!", getting_name, "to our Number Guessing Game")
main_block()
Game Initialization (main_block function):

The main_block function asks the user if they want to start the game.
If the user enters "yes," the number_guessing_game function is called.
If the user enters "no," the program exits.
If the user provides an invalid response, they are prompted to try again.

choice = input("Do you want to start this game [yes/no]:")
if choice.lower() == "yes":
    number_guessing_game()
elif choice.lower() == "no":
    print("Exit")
else:
    # Handling invalid responses
    while True:
        print("Type a proper reply for the request")
        choice = input("Do you want to start this game [yes/no]:")
        if choice.lower() == "yes":
            number_guessing_game()
        elif choice.lower() == "no":
            print("Exit")
            break
        else:
            print("Try again!!")
Number Guessing Game (number_guessing_game function):

The number_guessing_game function generates a random number as the computer's choice.
The user is prompted to guess the number, and the game provides feedback based on the correctness of the guess.
The user has multiple chances to guess, and the game terminates when they either guess correctly or run out of chances.

def number_guessing_game():
    # ... (Code for generating random number and handling user guesses)
User Interaction and Repetition:

After the game is completed, the user is asked if they want to play again.
If the user enters "yes," the game restarts; otherwise, the program exits.

choice = input("Do you want to start this game [yes/no]:")
if choice.lower() == "yes":
    number_guessing_game()
elif choice.lower() == "no":
    print("Exit")
else:
    # Handling invalid responses
    while True:
        print("Type a proper reply for the request")
        choice = input("Do you want to start this game [yes/no]:")
        if choice.lower() == "yes":
            number_guessing_game()
        elif choice.lower() == "no":
            print("Exit")
            break
        else:
            print("Try again!!")
Game Termination:

The program eventually exits after the user chooses not to play or after completing multiple rounds.

print("Exit")
This working pattern outlines the flow of the code, including user input, game initiation, gameplay, and repeated interactions. It provides a structure for the number guessing game, allowing users to enjoy multiple rounds and making decisions based on their inputs.

</p>

<h4> <span> · </span> <a href="https://github.com/MydeenRaahia/guess-the-number-game/blob/master/README.md"> Documentation </a> <span> · </span> <a href="https://github.com/MydeenRaahia/guess-the-number-game/issues"> Report Bug </a> <span> · </span> <a href="https://github.com/MydeenRaahia/guess-the-number-game/issues"> Request Feature </a> </h4>


</div>




## :star2: About the Project

## :handshake: Contact

MYDEENRAAHINA - - mydeenraahina862@gmail.com

Project Link: [https://github.com/mydeenraahina/guess-the-number-game](https://github.com/mydeenraahina/guess-the-number-game)
