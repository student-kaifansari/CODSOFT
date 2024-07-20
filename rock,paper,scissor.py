import random

def play_game():
    choices = ['rock', 'paper', 'scissor']
    
    while True:
        user_choice = input("Please,choose any one among rock, paper, or scissor: ").lower()
        if user_choice not in choices:
            print("Invalid choice. Please try again.")
            continue
        
        computer_choice = random.choice(choices)
        
        print(f'You chose: {user_choice}')
        print(f'Computer chose: {computer_choice}')
        
        if user_choice == computer_choice:
            print("It's a tie!")
        elif (user_choice == 'rock' and computer_choice == 'scissor'):
            print("You win!")
        elif (user_choice == 'scissor' and computer_choice == 'paper'):
            print("You win!")
        elif (user_choice == 'paper' and computer_choice == 'rock'):
            print("You win!")
        else:
            print("You lose!")
        
        play_again = input("Do you want to play again? (yes/no): ").lower()
        if play_again == 'yes':
            continue
        elif play_again == "no":
            break
        else:
            print("Invalid choice")
            break

    print('Thanks for playing!')
play_game()
