import random

options = ('Rock', 'Paper', 'Scissors')
player_points = 0
comp_points = 0
valid_choices = ['1', '2', '3']

print('Welcome to Rock Paper Scissors! \nFirst to 5 points wins.\n')

while True:
    player_num = input('Enter your choice:\n'
        + '1. Rock \n'
        + '2. Paper \n'
        + '3. Scissors \n\n')
        
    while player_num not in valid_choices:
        player_num = (input("Please enter a valid choice (1-3).\n"))

    player_num = int(player_num)

    player_choice = options[player_num - 1]
    comp_choice = options[random.randint(0,2)]

    print(f"Your choice: {player_choice}")
    print(f"Computer's choice: {comp_choice}")

    if player_choice == comp_choice:
        print("Tie!\n")
    elif (player_choice == 'Paper' and comp_choice == 'Scissors' or
        player_choice == 'Rock' and comp_choice == 'Paper' or
        player_choice == 'Scissors' and comp_choice == 'Rock'):
        print("You lost!\n")
        comp_points += 1
    elif (player_choice == 'Paper' and comp_choice == 'Rock' or
        player_choice == 'Rock' and comp_choice == 'Scissors' or
        player_choice == 'Scissors' and comp_choice == 'Paper'):
        print("You won!\n")
        player_points += 1
    
    print(f"Your points: {player_points} \n"
        + f"Computer's points: {comp_points} \n")
          
    if comp_points == 5 or player_points == 5:
        break
    else:
        continue     

if comp_points == 5:
    print("Better luck next time!")
else:
    print("You're too good ʕ•́ᴥ•̀ʔっ♡")
