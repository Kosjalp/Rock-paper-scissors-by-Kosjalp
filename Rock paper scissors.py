#Rock paper scissors
#By Kosjalp

#Import libraries
import time
import random
import getpass
import os
import datetime
#Define variables
wins = 0
ties = 0
losses = 0
computer_input = ("UNDEFINED")
choices = ["r", "p", "s"]
rounds = 0
#Get user data
user = getpass.getuser()
time_at_logon = datetime.datetime.now().replace(microsecond=0)
#Write files
if os.path.exists("history.txt"):
  pass
else:
  with open("history.txt", "w") as h:
    h.write("Rock paper scissors logon history: \n")
    h.write("\n")
with open("history.txt", "a") as h:
  h.write(f"User {user} logged on at date {time_at_logon}\n")
#Loading sequence
print("Welcome to rock paper scissors!")
time.sleep(1)
print("Let me set things up real quick...")
time.sleep(0.5)
print("...")
time.sleep(1)
print("-----.......")
time.sleep(0.8)
print("----------..")
time.sleep(0.5)
print("------------")
time.sleep(1)
print("Done!")
for i in range(3):
  print("")
print("Rock paper sissors")
print("©Kosjalp studios inc. (not actually)")
print("")
time.sleep(2)
for i in range(3):
  print("")
#Looping sequence
while True:
  player_input = input("Rock(r) paper(p) scissors(s) quit(q) or stats(i)? ") #Get user input
  computer_input = random.choice(choices) #Pick random computer input
  #Check winning/tying/losing
  if player_input == "r":
    if computer_input == "s":
      print("You win!")
      wins += 1
      rounds += 1
    elif computer_input == "p":
      print("You lost...")
      losses += 1
      rounds += 1
    elif computer_input == "r":
      print("It's a tie.")
      ties += 1
      rounds += 1
    else:
      for i in range(3):
        print("")
        print("Error01: Computer gave invalid input.")
        print("The computer is not computering")
      for i in range(3):
        print("")
  elif player_input == "s":
    if computer_input == "s":
      print("It's a tie.")
      ties += 1
      rounds += 1
    elif computer_input == "p":
      print("You win!")
      wins += 1
      rounds +=1
    elif computer_input == "r":
      print("You lost...")
      losses += 1
      rounds += 1
    else:
      for i in range(3):
        print("")
      print("Error01: Computer gave invalid input.")
      print("The computer is not computering")
      for i in range(3):
        print("")
  elif player_input == "p":
    if computer_input == "s":
      print("You lost...")
      losses += 1
      rounds += 1
    elif computer_input == "p":
      print("It's a tie.")
      ties += 1
      rounds += 1
    elif computer_input == "r":
      print("You win!")
      wins += 1
      rounds +=1
  #Stats section
  elif player_input == "i":
    print("Stats:")
    print("")
    print("Wins", wins)
    print("Losses", losses)
    print("Ties", ties)
    print("")
    score = float((wins+1)/((losses+1)*2)+(ties/2)-(losses/2)) #Calculate overall score
    print("Overall score:", score)
  #Quitting
  elif player_input == "q":
    print("Manual quit")
    for i in range(3):
      print("")
    quit("Thanks for playing!")
  #Error
  #Error01: Computer gives invalid input
  #Error02: Player gives invald input
  else:
    for i in range(3):
      print("")
    print("Error02: Invalid input.")
    print("I don't understand... There's clearly a misunderstanding...")
    for i in range(3):
      print("")
