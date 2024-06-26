import random

def main():
    print("Welcome to Rock, Paper, Scissors!")
    while True:
        user_choice = input("Choose rock, paper, or scissors: ").lower()
        computer_choice = random.choice(['rock', 'paper', 'scissors'])
        
        print("You chose:", user_choice)
        print("Computer chose:", computer_choice)
        
        if user_choice == computer_choice:
            print("It's a tie!")
        elif (user_choice == 'rock' and computer_choice == 'scissors') or \
             (user_choice == 'scissors' and computer_choice == 'paper') or \
             (user_choice == 'paper' and computer_choice == 'rock'):
            print("You win!")
        else:
            print("Computer wins!")
        
        play_again = input("Do you want to play again? (yes/no): ").lower()
        if play_again != 'yes':
            print("Thanks for playing!")
            break

if __name__ == "__main__":
    main()
