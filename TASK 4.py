import random
Human_points = 0
bot_points = 0
while True:
    print("\nRock, Paper, Scissors Game")
    print("Choose your option:")
    print("1. Rock")
    print("2. Paper")
    print("3. Scissors")
    UC= input("Enter your choice (1/2/3): ")  #UC = User Choice
    if UC not in ['1', '2', '3']:
        print("Invalid choice. Please try again.")
        continue
    if UC== '1':
        UCN = 'Rock'
    elif UC== '2':
        UCN = 'Paper'
    elif UC== '3':
        UCN = 'Scissors' #UCN = user choice name
    computer_choice = random.choice(['1', '2', '3'])
    if computer_choice == '1':
        CCN = 'Rock'#CCN = computer choice name
    elif computer_choice == '2':
        CCN = 'Paper'
    elif computer_choice == '3':
        CCN = 'Scissors'
    print(f"\nYou chose: {UCN}")
    print(f"Computer chose: {CCN}")
    if UC== computer_choice:
        print("It's a tie!")
    elif (UC== '1' and computer_choice == '3') or (UC== '2' and computer_choice == '1') or (UC== '3' and computer_choice == '2'):
        print("You win!")
        Human_points += 1
    else:
        print("You lose!")
        bot_points += 1
    print(f"Scores: You - {Human_points}, Computer - {bot_points}")
    play_again = input("\nDo you want to play again? (y/n): ").lower()
    if play_again != 'y':
        print("Thanks for playing!")
        break
