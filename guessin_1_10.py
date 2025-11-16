# While loop is the magic in this task so don't understimate it#########################################################

# fuction for the computer move
from random import randint

def computer_choice():
    computer_choice=''

    computer_choice = randint(1,10)
    
    return computer_choice



# function for the player choice
def player_choice():
    choice=''

    while choice.isdigit()== False or int(choice) not in range(1,11):
        choice = input("choose a number between 1 to 10")
        
# digit check
        if choice.isdigit() == False:
            print('digit not string')

# Range check
        if choice.isdigit() == True:
            if int(choice) not in range(1,11):
                print('Please. Number between 1 to 10')

    return int(choice)



# fuction to see if the player choosed the right number as the computer
def check(computer_choice_num, player_choice_num):
   
    attempts = [player_choice_num]  # start with the first guess

    # check the initial guess
    # while loop to keep looping until he/she answer the right answer########################################################
    while player_choice_num != computer_choice_num:
        print('We need more tries until you get it correct.')
        player_choice_num = player_choice()  # ask for new guess
        attempts.append(player_choice_num)

    return (len(attempts))  # returns correct guess and attempts



# logic
# Step 1: Computer chooses a number
computer_num = computer_choice()

# Step 2: Player makes the first guess
first_guess = player_choice()

# Step 3: Check the guess (looping inside check)
total_tries = check(computer_num, first_guess)

# Step 4: Show the result
print(f'You got it right after {total_tries} tries!')
