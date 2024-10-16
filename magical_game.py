'''
Author: acbart (2/6/2019)
Version: 1
Co-author: _Dina Dawood_ (09/09/2019)

1. Give a brief description of how the code below works.
   Use plain, accessible language and avoid repeating
   the exact statements from the code. Aim to write at
   least 3 sentences.
   
   __The program below is designed based on the Wizard101 theme.
   When running the code, the console will first ask for the users username.
   After the user has given a reply, the program will greet the user and,
   then introduce the rules of the game. Basically, the user has to guess
   the correct number that the computer is thinking of, while the computer
   will provide additional hints such as going higher or lower.__

2. Make a modification to the code in some place that changes the game
   in some interesting way. This cannot be as simple as changing the
   MINIMUM or one of the printed messages, but make enough changes and
   they can add up. You might allow the player to play more rounds after
   the first one, or completely change all the messages to have a pirate
   theme, or make it so the player can specify the maximum number.
   Describe your change here clearly and explain why you thought it was
   interesting.
   
   __As for the changes I have inputted in the code below, I decided on
   changing the theme of the game to something I was interested in as
   a child. I made the theme based on the multiplayer role game, Wizard101.
   The responses to the users replies are all set to be somewhat similar to
   the original game. I also decided to change the minimum and maximum's of the game
   to my favorite numbers. I thought it was interesting to make this theme
   since I have always been curious about how the creators designed the
   processes and codes of the game and basically wanted to try something
   similar myself. __

'''

# Import the randint function generate random integers
from random import randint

# Establish the lower and uppper bound on the goal number
MINIMUM = 5
MAXIMUM = 75

def print_welcome():
    '''
    Prompt the user for their Wizard101 username, and then display a
    simple message explaining the rules of the game.
    '''
    # Get the name of the user
    name = input("What is your Wizard101 username? ")
    # Show the user's name
    print("Hello", name, "and greetings to my magical game.")
    # Print out the limits of the goal number
    print("I am thinking of a number between", MINIMUM, "and", MAXIMUM)
    # Write out rest of the instructions
    print("You will have to magically guess the correct number to pass this level.")
    print("I will tell you if you need to go higher or lower to succeed.")
    
def print_ending():
    '''
    Print out a conclusive message to wrap up the game.
    '''
    print("Good job young wizard! You have achieved the first level of the magic school, but don't get too excited now, there will be many more.")
    
def process_guess(guess, goal):
    '''
    Print out whether or not the user was above, below,
    or at the goal.
    
    Args:
        guess (int): The number that the user entered
            as their guess.
        goal (int): The number that the computer is
            thinking of.
    '''
    # Branch execution based on whether the guess was right
    if guess < goal:
        print("You need to move higher than that!")
    elif guess > goal:
        print("How about going lower?!")
    else:
        print("Bravo young wizard, it's", goal)

def get_number():
    '''
    Ask the user for a number, and keep prompting
    them until they give you an actual number
    (as opposed to giving you a letter).
    '''
    # Get the guess from the user, returns a string
    number = input("What do you predict young wizard? ")
    # Was the string composed only of numbers?
    if number.isdigit():
        # If so, we can safely convert it to an integer
        number_as_int = int(number)
        # And return the result
        return number_as_int
    else:
        # Otherwise, call this function again recursively
        return get_number()

def main_game():
    '''
    Play a round of the game.
    '''
    # Pick random number between MINIMUM and MAXIMUM
    goal = randint(MINIMUM, MAXIMUM)
    # Initially, the user hasn't guessed anything.
    user_guess = None

    print_welcome()
    # Repeatedly ask the user until they get it right
    while user_guess != goal:
        user_guess = get_number()
        process_guess(user_guess, goal)
    print_ending()

# This if statement is common in most professional Python
#   programs - don't worry too much about what it does,
#   but you can safely assume it will work when you press
#   the run button.
if __name__ == '__main__':
    main_game()