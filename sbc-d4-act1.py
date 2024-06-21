from random import randint # randint is for randomizing the number of the given numbers
"""
Welcome to the Kulob and Hayang Game 
or 
the Fold and Unfold Game
'''''''''''''''''''''''''''''''''
Fold (-----)
Unfold (*****)
_________________________________________________________________________________________________________ """
choices_1, choices_2 = "-----" , "*****" # The choices

while True: # To execute the code repeatedly
        
    randon_Number_Computer_1 = randint(1,2) # Randomize the given number and stored it to the randon_Number_Computer_1 variable
    randon_Number_Computer_2 = randint(1,2) # Randomize the given number and stored it to the randon_Number_Computer_2 variable

    if randon_Number_Computer_1 == 1 and randon_Number_Computer_2 == 1: # If the two condition are TRUE then it execute the statement comes next to this line
        computer_1 = computer_2 = choices_1 # Computer 1 and 2 are Fold

    elif randon_Number_Computer_1 == 2 and randon_Number_Computer_2 == 2: # If the two condition are TRUE then it execute the statement comes next to this line
        computer_1 = computer_2 = choices_1 # Computer 1 and 2 are Unfold

    elif randon_Number_Computer_1 != 1 and randon_Number_Computer_2 == 1: # If the two condition are TRUE then it execute the statement comes next to this line
        computer_1, computer_2 = choices_2 , choices_1 # Computer 1 is Unfold then Computer 2 is Fold

    else:
        computer_1, computer_2 = choices_1 , choices_2 # Computer 2 is Unfold then Computer 1 is Fold
    print("------------------------------------------------")
    userInput = input("Choose Fold or Unfold > ")  # Take input from the Users or Player

    if userInput.capitalize() == "Fold": #if user choose fold then it execute the statement below
        player = choices_1 # store the choices 1 to the player
        exit # Continue and exit the While True statement
    elif userInput.capitalize() == "Unfold": # if user choose unfold then it execute the statement below
        player = choices_2 # store the choices 2 to the player
        exit # Continue and exit the While True statement
    else:
        print("Wrong input") # show the user that the input is wrong then it go back to the user inputs
        continue
    print(f"""
    Player choose {player}
    Computer 1 choose {computer_1}
    Computer 2 choose {computer_2}
__________________________________________________________
    """) # Display what the players (including player, and the computers) choose

    if (player == choices_1 and computer_1 == choices_2 and computer_2 == choices_2) or (player == choices_2 and computer_1 == choices_1 and computer_2 == choices_1): # If player didnt choose what the computers has choosen, then he/she wins
        print("Player 1 Win!!!!")

    elif (player == choices_2 and computer_1 == choices_1 and computer_2 == choices_2) or (player == choices_1 and computer_1 == choices_2 and computer_2 == choices_1): # If Computer 1 didnt choose what the player and computer 2 has choosen, then it wins
        print("Computer 1 Win!!!!")

        
    elif (player == choices_2 and computer_1 == choices_2 and computer_2 == choices_1) or (player == choices_1 and computer_1 == choices_1 and computer_2 == choices_2):# If Computer 2 didnt choose what the player and computer 1 has choosen, then it wins
        print("Computer 2 Win!!!!")
        
    
    else:
        print("No one wins") #print no one wins if the 3 players chooses the same choices

    q_or_g = input("Type q if you want to quit the game, if no type g > ")

    if q_or_g.lower() == "q":
        print("Thankyou for Playing")
        break
    elif q_or_g.lower() == "g":
        print("Enjoy Playing")
        continue
    else:
        print("What?")



