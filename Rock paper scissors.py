#Rock paper scissors
#By Kosjalp

#Import libraries
import time
import random
import getpass
import os
import datetime
import shutil
from pathlib import Path
from updatesavedata import updatesavedata
from updateregulardata import updateregulardata
#Define variables
wins = 0
ties = 0
losses = 0
computer_input = ("UNDEFINED")
choices = ["r", "p", "s"]
rounds = 0
money = 0
combo_wins = 0
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
if os.path.exists("save_data"):
  pass
else:
  Path("save_data").mkdir(exist_ok=True)
with open("history.txt", "a") as h:
  h.write(f"User {user} logged on at date {time_at_logon}\n")
money, wins, losses, ties = updateregulardata()
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
print("Rock paper scissors")
print("©Kosjalp studios inc. (not actually)")
print("")
time.sleep(2)
for i in range(3):
  print("")
#Looping sequence
while True:
  player_input = input("play(p) quit(q) stats(s) reset(r), clear cache(e) or credits(c)? ") #Get user input
  #Playing sequence
  if player_input == "p":
    while True:
      computer_input = random.choice(choices) #Pick random computer input
      player_input = input("Rock(r), paper(p), scissors(s), or leave playing(q)? ") #See what the player wants to play
      pre_wins = wins #For combo detection
      #Playing sequence
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
            print(f"(Computer gave {computer_input})")
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
            print(f"(Computer gave {computer_input})")
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
          rounds += 1
        else:
          for i in range(3):
            print("")
            print("Error01: Computer gave invalid input.")
            print("The computer is not computering")
            print(f"(Computer gave {computer_input})")
          for i in range(3):
            print("")
      #Leave playing
      elif player_input == "q":
        print("")
        print("Leave playing chosen... returning to main menu.")
        print("")
        print("")
        break
      else:
        for i in range(3):
          print("")
        print("Error02: Invalid input.")
        print("I don't understand... There's clearly a misunderstanding...")
        for i in range(3):
          print("")
      #Find combos
      if pre_wins != wins:
        money += 1
        combo_wins += 1
        if combo_wins == 3:
          money += 3
          print("3 Combo! Nice!")
        elif combo_wins == 5:
          money += 6
          print("5 Combo! Not bad!")
        elif combo_wins == 7:
          money += 10
          print("7 Combo! Good job!")
        print(f"You now have {money}$")
      elif pre_wins == wins:
        combo_wins = 0
      updatesavedata(wins, money, losses, ties) #Update save data
  #Stats section
  elif player_input == "s":
    print("Stats:")
    print("")
    print("Wins", wins)
    print("Losses", losses)
    print("Ties", ties)
    print("")
    print(f"You have {money}$.")
    print("")
    score = float((wins+1)/((losses+1)*2)+(ties/2)-(losses/2)) #Calculate overall score
    print("Overall score:", score)
  #Quitting
  elif player_input == "q":
    print("Manual quit")
    for i in range(3):
      print("")
    quit("Thanks for playing!")
#Deleting data
  elif player_input == "r":
    player_input = input("Are you sure you want to reset the game? (Y/N) ") #Confirmation 1
    if player_input == "y":
      player_input = input("Are you really sure? (Y/N) ") #Confirmation 2
      if player_input == "y":
        print("Ok then.")
        #Deleting files, variables and folders
        #Delete folders
        if os.path.exists("save_data"):
          shutil.rmtree("save_data")
        #Reset variables
        money = 0
        wins = 0
        ties = 0
        losses = 0
        rounds = 0
        #Deleting sequence
        print("Deleting data...")
        time.sleep(1)
        print("Deleting stats...")
        time.sleep(1)
        print("Deleting history.txt...")
        time.sleep(2)
        print("Done!")
        time.sleep(2)
        #Skip a bunch of lines
        for i in range(100):
          print("")
    #Cancel reset
      else:
        print("Cancel reset...")
        print("")
    else:
      print("Cancel reset...")
      print("")
  #Clearing cache
  elif player_input == "e":
    player_input = input("Are you sure you want to clear the cache? Theres nothing big, but it will clear your logon data AKA History.txt. (Y/N) ") #Confirm
    if player_input == "y":
      computer_input = ("UNDEFINED")
      combo_wins = 0
      player_input = 0
      pre_wins = 0
      if os.path.exists("__pycache__"):
        shutil.rmtree("__pycache__")
      if os.path.exists("history.txt"):
          os.remove("history.txt")
      #Cache clear sequence
      print("Clearing cache...")
      time.sleep(1)
      print("Deleting files...")
      time.sleep(1.5)
      print("Deleting __pycache__...")
      time.sleep(0.5)
      print(".")
      time.sleep(0.5)
      print("..")
      time.sleep(0.5)
      print("...")
      time.sleep(1)
      print("Done!")
      time.sleep(1)
      for i in range(4):
        print("")
  #Credits section
  elif player_input == "c":
    time.sleep(1)
    print("Credits:")
    print("")
    time.sleep(1)
    print("Made by Kosjalp on github")
    print("https://github.com/Kosjalp")
    print("")
    time.sleep(2)
    print("Hosted on GitHub")
    print("https://github.com/Kosjalp/Rock-paper-scissors-by-Kosjalp")
    print("")
    time.sleep(2)
    print("Thank you to:")
    time.sleep(1)
    print("Techspark academy for inspiration")
    time.sleep(1)
    print("")
    print("")
    time.sleep(1)
    print("Thanks for playing!")
    for i in range(3):
      print("")
  else:
  #Error
  #Error01: Computer gives invalid input
  #Error02: Player gives invald input
    for i in range(3):
      print("")
    print("Error02: Invalid input.")
    print("I don't understand... There's clearly a misunderstanding...")
    for i in range(3):
      print("")
