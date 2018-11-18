# Cody Young
# Sara Kazemi
# SCSI Logic
# Lab 10
# 2018-11-20

# Warmup
# Demonstrates requestString(), user input, and output.
def warmup():
  uinput = requestString("What is your name?")
  printNow(uinput)
  
  #Requests user input in a while loop. Stops when user types in string "stop".
  while(1):
    uinput = requestString("What is your name?")
    if uinput != "stop":
      printNow(uinput)
    else:
      printNow("Exiting loop.")
      break 
# -------
# Hangman
# -------
# A fully functional game of hangman.

# Used for testing/running game. 
def main():
  menu()
  game()
  

# Runs the actual hangman game.
def game():
  #Instance variables
  
  #Number of guesses user has
  guesses = 0
  user_guess = requestString("Guess a letter:")
  
  #List to hold incorrect guesses
  incorrect_guesses = []
  #Winning phrase
  phrase = "chocolate"
  
  #While guesses <= 6:
  #Get user input (NOT case sensitive) 
  #Check for fault conditions
  
  #If clear of fault conditions, check if letter is in phrase
  #If true(in phrase), print letter and "Correct!" guess message
  #If false(not in phrase), add letter to incorrect guesses,
  #print "Incorrect!" message, update incorrect gusses, print previous state
  #Increment guesses counter if necessary
  #Check for win/lose game condition
  
# Draws the main menu.
def menu():
  print("-----------------")
  print("|HANGMAN|")
  print("-----------------")
  print("Welcome to Hangman!")
  print("Guess the word or phrase correctly before you run out of attempts.\n")

#Checks user guess for fault conditions.
#def errorCheck(guess):
  #Fault conditions:
  #1. User does not enter an alphabetic char
  #2. User enters letter previously guessed
  #3. User enters more than one char at a time
    



