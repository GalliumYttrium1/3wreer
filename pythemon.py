import random #imports the random library
playerhealth = 100 #sets the players health at 100
cpuhealth = 100 #sets the computers health at 100
#prints the game title
print(''' 
__________          __  .__                                   
\______   \___.__._/  |_|  |__   ____   _____   ____   ____   
|     ___<   |  |\   __\  |  \_/ __ \ /     \ /  _ \ /    \ 
|    |    \___  | |  | |   Y  \  ___/|  Y Y  (  <_> )   |  \ 
|____|    / ____| |__| |___|  /\___  >__|_|  /\____/|___|  / 
          \/                \/     \/      \/            \/ 
''')
#briefly explains some information about the game
print('Welcome to Pythemon, an RPG, python implemented, game where you are able to battle Pokemon, my name is Jake and I will be you opponent') #this print function explains some of my game to the player
print('''
around here we have a couple rules
1. Your attacks must all have a maximum of 20 damage
2. No running or switching pokemon, this is pythemon not pokemon ruby, ok...the dev isnt that talented at coding
3. No whining after I kick your ass
''')

#this print function displays the possible option to choose from, that being Pikachu, Slowpoke, and Blatoise
print('''
Pikachu:                             
Slowpoke:
Charmander:                                    
''')
choose_pokemon = input('What pokemon would you like to adopt? ') #this input statement asks for what pokemon you would like to equip
pokemon = ['Pikachu', 'Slowpoke', 'Charmander'] #this is what the player and computer choose from
print("You have chosen",choose_pokemon) #this confirms what pokemon you chose
cpu_pokemon = random.choice(pokemon) #this allows the cpu to choose its pokemon through the implention of the random function, imported before
print('Your opponent has chosen ', cpu_pokemon) #this print statement declares the opponents pokemon through the variable set before
print('MATCH BEGIN!') #this is an extremely easily implemented print statement with the sole purpose of declaring the match

#____________________________________________________________________________________________________________________________________________________________________________________________________________________________________________
#                                                                                                       ATTACK
#____________________________________________________________________________________________________________________________________________________________________________________________________________________________________________

#this shows teh user the attack choices
print ('''ATTACKS:
1. Bolt Strike - Damage 10 - 20
2. Body Slam - Damage 10 - 20
3. Mud Slide - Damage 10 - 20
4. Tail Whip - Damage 10 - 20''')

#loops the attacks and data validation system
while playerhealth>=0 and cpuhealth>=0:
#asks what move they would like to pick
        moves = input('Which move would you like to choose?')
#says if they choose 1, 2, 3, 4 the code will let them adavance - if not the code will repeat again
        if moves == '1' or moves == '2' or moves == '3' or moves == '4':
#create a random number for the attack damage 
                moves = random.randint(10, 20)
#takes the damage line above and subtracts it from the cpu pokemon health
                cpuhealth = cpuhealth - moves
#shows how much damage was done and how much health the pokemon has left
                print (moves, "was dealt to the CPU's pokemon. His health is", cpuhealth)
#creates a random intager for the cpu attack
                cpu_move = random.randint(10, 20)
#the intager created above creates a damage which is then taken from the player 1 health
                playerhealth = playerhealth - cpu_move
#shows the damage done and the health left in pokemon1
                print ('The CPU has attacked you!!! It has done', cpu_move, 'Your pokemon health is', playerhealth)
#reset the cpu_move so its ready for the next attack
                cpu_move = 0
#this else staement collects the inappropriate responses
        else:
                print('That is not an option, try again') #this prints that the user has made an error

#declares teh winner by who reaches 0 or less health first
        again = 0
        if cpuhealth <= 0:
                print("You Won")
                break
        elif playerhealth <= 0:
                print("You Lost")
                break

        
 




    
