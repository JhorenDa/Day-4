from random import randint # import the randint 

result = randint(1, 999) # pick random number in the range of 1 to 999
result_formatted = f"{result:03d}" # formatted the random pick to always have a 3 digits number, If the result is 25 then the format is 025


print(f"The Jackpot is {result_formatted}.") # print the possible result

user = input("Give Three numbers that you feel it is gonna win > ") # take user input

if user == result_formatted: # if condition met then it print the winning message
    print("Congratulations! Its a Win Win Win, You won 1 million Dollars.")

elif (sorted(user) == sorted(result_formatted)) : # it sort the user inputs and the result to least number to higher number so that the it is easy for the programm to compare if the player wins the scramble
    print("Congratulations! You win Scramble, you still win small Prize")

elif len(user) >= 4: #if it input more than or equal to 4 then it tells the user or player that he inputed a lot of numbers
    print("You inputed a lot of numbers")
elif len(user) <= 2: # if it input numbers (0 to 2) then it tells that user or player that he inputed insufficient numbers
    print("You inputed insufficient numbers")

else: #this is when the user or player did'nt win The Jackpot or The Scramble number, this means he lose. The programm then tells the user or player that he didnt won.
    print(f"Sorry You lose!!, Better Luck Next Time {result}.")
