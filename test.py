import random

def get_user_choice():
    choice = input('enter rock , paper or scissors')
    if choice in ('rock' ,'paper', 'scissors'):
        return choice
    else:
        print ('invalid choice')
        return  get_user_choice()                             
    

def get_computer_choice():
    return random.choice (['rock','paper','scissors'])

def determine_winner(user,computer):
    if user == computer:
        return 'its a tie'
    elif ({user == 'rock' and computer == 'scissors'}or\
       {user == 'scissors'and computer == 'paper'}or\
       {user == 'paper'and computer == 'rock'}):
        return "you win"

    else:
        return 'computer wins'
    
def play_game():
    print ('welcome to the game')
    while True:
        user_choice = get_user_choice()
        computer_choice = get_computer_choice()
        print(f"\nYou chose: {user_choice}")
        print(f"Computer chose: {computer_choice}")
        result = determine_winner(user_choice,computer_choice)
        print(f'\n result {result}')
        play_again = input("\nPlay again? (yes/no): ").strip().lower()
        if play_again != 'yes':
            print("Thanks for playing!")
            break

# Run the game
if __name__ == "__main__":
    play_game()