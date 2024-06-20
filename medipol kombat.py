import random
#Lists will be used to store players attributes
#Also asks for input for the names of the players
player1 = [input(f"----First Hero----\n Player 1 please enter a name: "), 100, False]
player2 = [input(f"----Second Hero----\nPlayer 2 please enter a name: "), 100, False]

def name_selection():
    #This function checks names are in wanted format or not
    while True:
        if player1[0] == '':
            player1[0] = input('Wrong selection,player 1 please enter name!!!!:')
        if player2[0] == '':
            player2[0] = input('Wrong selection,player 2 please enter name!!!!:')
        if player1[0] == player2[0]:
            player2[0] = input('Names are cannot be same. Player 2 please enter another name:')
        else:
            break

def decide_first_attacker():
    #This function randomly picks the first attacker from the players list.
    players = [player1[0],player2[0]]
    first_attacker = random.choice(players)
    print(f'{first_attacker} is the starter!!')
    if first_attacker == player1[0]:
        player1[2] = True
    else:
        player2[2] = True

def healths():
    #This function displays the player's health points in a bar format.
    spaces = (player1[1] // 2)
    if spaces < 1:
        spaces = 1

    print(f"{player1[0]} HP:[{player1[1]}]", end='')
    print(' ' * spaces, end='')
    print(f"{player2[0]} HP:[{player2[1]}]")

    for i in range((player1[1] + 1) // 2):
        print('|', end='')

    print(' '*12, end='')

    for i in range((player2[1] + 1) // 2):
        print('|', end='')
    print()

def give_attack_magnitude(attacker):
    #This function requests a valid attack magnitude between 1 and 50 from the attacker.
    while True:
        magnitude_str = input(f"{attacker[0]}'s turn.Enter an attack magnitude:")
        if magnitude_str.isdigit(): #isdigit checks magnitude_str has only digits or not
            magnitude = int(magnitude_str) #Converts the string to an integer
            if 1 <= magnitude <= 50 :
                return magnitude
            else:
                print("The magnitude must be between 1 and 50. Try another number: ")
        else:
            print("The magnitude must be between 1 and 50. Try another number: ")

def attack(attacker,defender,attack_magnitude):
 #This function gives an attack magnitude based on the success rate.
    success_chance = 100-attack_magnitude
    attack_success = random.randint(1,100)<=success_chance
    if attack_success == True :
        print(f"{attacker[0]} hit {attack_magnitude} to {defender[0]}")
        if attacker == player1:
            player2[1] -= attack_magnitude
        else:
            player1[1] -= attack_magnitude
    else:
        print(f"upsss!!!{attacker[0]}'s attack missed")

def winner(winner_name):
    #This function prints winner name
     print(f"{'#' * 27}\n{'#' * 5} {winner_name[0]} is win !!! {'#' * 5}\n{'#' * 27}")


while True:
    #start a new game loop
    name_selection()
    print()
    print('Game is starting,good luck ;)')
    print()

    player1[1] = 100 #in these part players healths are changing for new round
    player2[1] = 100
    decide_first_attacker()
    print()
    healths()
    print()
    #Main game loop starts
    while player1[1] > 0 and player2[1] > 0 : #If players healths bigger than 0 loop is continue
        if player1[2] == True:  #Player 1's turn
            attack_magnitude = give_attack_magnitude(player1)
            attack(player1,player2,attack_magnitude)
            player1[2] = False #switch turn to player2
        else:      #Player 2's turn
            attack_magnitude = give_attack_magnitude(player2)
            attack(player2,player1,attack_magnitude)
            player1[2] = True  #switch turn to player1

        healths()
        print()
    #The winner is decided in this part
    if player2[1] <= 0:
        winner_name = player1
    else:
        winner_name = player2

    winner(winner_name) #Print winner


    #ask for another game
    play_again = input('Do you want to play another game? yes/no  ').lower()
#lower makes all characters lowercase,so there would be no confusion if answer has capital letter
    if play_again != 'yes' :
        print('Thanks for playing GG see you soon.')
        break











