import random #to generate random computer choice from list, rps
import time #to put in wait times if necessary
plays = int(input('How many wins will it take to win the game? ')) #best x
maxplays = int(input('Out of? ')) #out of y
maxconstant = int(maxplays) #this resets maxplays at the end of a game and allows next game to track rounds remaining
choices = ["rock", "paper", "scissors"] #user choices
rps = ["Rock","Paper","Scissors"] #computer choices


score = 0 #start score
idiotpoint = 0 #score for times youve messed up input
compscore = 0 #initial computer score
round = 0 #first round
yn = True #this is the default value to start the loop
victories = {"rock":"Scissors", "scissors": "Paper", "paper": "Rock"}
while yn == True:
     round = round + 1 #counts rounds
     choice = input('What are you going to throw? ') #user input
     choice = choice.lower() #formats user input into same format as "choices" list
     comp =  random.choice(rps) #assigns computer choice randomly

     if choice == 'quit': #ends game when user types quit
         break
     elif choice not in choices:
         print(choice,"ain't gonna work against",comp,"buddy!")
         print("Get out of here!")
         print("")
         idiotpoint = idiotpoint+1
     elif comp.lower() == choice:
         print("you and the computer both threw " + choice.capitalize() + ", so it was a tie game!")
     elif comp == victories[choice]:
        print("you threw " + choice.capitalize(), "and the computer threw " + comp + ", so you win")
        score = score + 1
     elif comp != victories[choice]:
        print("you threw " + choice.capitalize(), "and the computer threw " + comp + ", so you lose!")
        compscore = compscore + 1
        # #this block tallies a score for when input is messed up and tells the user

     print("Round " + str(round) + " summary: ")
     print("Your Score:", score)
     print("Comp Score:", compscore)
     print(" ")
     print(" ")
     maxplays = maxplays - 1 #counts down games remaining regardless of which conditional is true (tie, win, or lose)
     if idiotpoint != 0: #only includes 'times you messed up' score if it happens
         print("")
         print("Times you've messed up:", idiotpoint)
     print("Games Remaining:", maxplays)

#     #block below says if you win or lose
     if maxplays == 0 or (score == plays or compscore == plays):
         if compscore > score:
             print("YOU LOSE THE GAME!")
         if compscore < score:
             print("YOU WIN THE GAME!")
         if compscore == score:
             print("IT'S A TIE GAME!")

         yn = input('Would you like to play again? ')
         yn = yn.lower() #formats user input to match options for 'yn' below
#         #if yes, block below resets game stats and rounds to original selection
         if yn == 'yes' or yn == 'yeah' or yn == 'yes'or yn == 'absolutely':
             score = 0
             idiotpoint = 0
             compscore = 0
             round = 0
             maxplays = maxconstant #sets rounds remaining to original maxplays from user input
             yn = True
         else: #if user doesnt want to play again (input different than any options in block above, loop ends)
             yn = False
