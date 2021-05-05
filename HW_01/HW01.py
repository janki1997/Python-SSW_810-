#  Replace all of the 'TODO:' sections with your code.


from random import choice

def get_human_move() -> str:
    """ Ask the user for R, P, or S.  Loop until given a valid input """
    while True:
        #convert all the data in to lower case so when we write in capital it will automatically convert in to lowercase.
        user_input: str = input("Please choose 'Rock', 'Paper', 'Scissors','R','S','P','Q' or 'Quit' to quit: ").lower()
        print("Human choose:",user_input)
    
        return user_input
        
        # """ TODO: convert the user's input to 'rock', 'paper', 'scissors', 'quit' and return the string 
        #  Print an error message and loop again if the user inputs an invalid input value.
        # """

def get_computer_move() -> str:
    """ return the computer's random choice using random.choice """
    #convert all the data in to lower case so when we write in capital it will automatically convert in to lowercase.
    move: str = choice(['Rock', 'Paper', 'Scissors']).lower()
    print("computer:",move)
    return move  
        
def play_game() -> bool:
    """ play Rock/Paper/Scissors
        The human may enter 'Q' or 'q' any time to stop the game.
        Get the human's move, the computer's move, and print a message with the winner.
        Return a bool to specify if the human wants to play again, 
        i.e. False when the human wants to quit or True to play again
    """
    human: str = get_human_move()
    # When human wants to quit the game.
    if human == 'quit' or human == 'q':  # human wants to quit
        return False

    computer: str = get_computer_move()
    #When human choose paper on that time what happen
    if human == "paper" or human == 'p':
        if computer == "scissors":
            print( computer, "beats", human,"So,Computer win the game.")
        elif computer == "rock":
            print(human, "beats", computer,"So,Human You win the game." )
        else:
            print("Yehhhh it's tiee")
    #When human choose rock or r on that what happen 
    elif human == "rock" or human =='r' :
        if computer == "paper":
            print( computer, "beats", human,"So,Computer You win the game.")
        elif computer == "scissors":
            print(human, "beats", computer,"So,Human You win the game. ")
        else:
            print("Yehh It's Tie!!")
    #when human choose scissors on that what happen with result
    elif human == "scissors" or human == 's':
        if computer == "rock":
            print( computer, "beats", human,"So,Human You win the game.")
        elif computer == "paper":
            print( human, "beats", computer,"So,Human You win the game.")
        else:
            print("Yehh It's Tei!!!!")

    #when data is wrong 
    else:
        print("Check your spelling or DataType and Try Again!!!")
    
    """ TODO: your logic to determine the winner goes here """

    return True  # play again

def main() -> None:
    """ Play multiple games until the human asks to stop """
    again: bool = True
    while again:
        again = play_game()
        
    print("Thanks for playing!")

if __name__ == "__main__":
    main()