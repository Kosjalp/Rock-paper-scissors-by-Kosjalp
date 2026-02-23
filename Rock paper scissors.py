#Rock paper scissors
#By Kosjalp

#Import libraries
import time
import random
import getpass
import os
import datetime
import shutil
import platform
from pathlib import Path
from updatesavedata import updatesavedata
from updateregulardata import updateregulardata
from playsound import playsound
#Define variables
wins = 0
ties = 0
losses = 0
computer_input = ("UNDEFINED")
choices = ["r", "p", "s"]
achievements = []
rounds = 0
money = 0
combo_wins = 0
operating_system = platform.system()
playsoundfilepath = 0
pre_losses = 0
combo_losses = 0
#Get user data
user = getpass.getuser()
time_at_logon = datetime.datetime.now().replace(microsecond=0)
#Find OS
if operating_system == "Darwin":
  user_os = "Mac"
elif operating_system == "Windows":
  user_os = "Windows"
elif operating_system == "Linux":
  user_os = "Linux"
else:
  print("Unknown operating system. Some functionalities such as sound may be limited.")
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
money, wins, losses, ties, achievements = updateregulardata()
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
playsound(user_os, playsoundfilepath=os.path.join("assets", "startup.wav"))
for i in range(3):
  print("")
#Looping sequence
while True:
  player_input = input("play(p) quit(q) stats(s) reset(r), clear cache(e), credits(c) or achievements(a)? ") #Get user input
  #Playing sequence
  if player_input == "p":
    while True:
      computer_input = random.choice(choices) #Pick random computer input
      player_input = input("Rock(r), paper(p), scissors(s), or leave playing(q)? ") #See what the player wants to play
      pre_wins = wins #For combo detection
      pre_losses = losses
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
      #Invalid input
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
      if pre_losses != losses:
        combo_losses += 1
      elif pre_losses == losses:
        combo_losses = 0
      #Check for achievements
      if wins == 1 and "First win: Get a win" not in achievements:
        print("")
        print("Achievement unlocked: First win")
        print("")
        achievements.append("First win: Get a win")
      if wins == 10 and "Winner: Win ten times" not in achievements:
        print("")
        print("Achievement unlocked: Winner")
        print("")
        achievements.append("Winner: Win ten times")
      if wins == 25 and "Champion: Get 25 wins" not in achievements:
        print("")
        print("Achievement unlocked: Champion")
        print("")
        achievements.append("Champion: Get 25 wins")
      if combo_wins == 3 and "3 in a row: Get a combo of 3" not in achievements:
        print("")
        print("Achievement unlocked: 3 in a row")
        print("")
        achievements.append("3 in a row: Get a combo of 3")
      if combo_wins == 5 and "Lucky: Get a combo of 5" not in achievements:
        print("")
        print("Achievement unlocked: Lucky")
        print("")
        achievements.append("Lucky: Get a combo of 5")
      if combo_wins == 7 and "Lottery lucky: Get a combo of 7" not in achievements:
        print("")
        print("Achievement unlocked: Lottery lucky")
        print("")
        achievements.append("Lottery lucky: Get a combo of 7")
      if combo_losses == 3 and "Unlucky: Lose 3 times in a row" not in achievements:
        print("")
        print("Achievement unlocked: Unlucky")
        print("")
        achievements.append("Unlucky: Lose 3 times in a row")
      if wins == 50 and "King of the wins: win 50 times" not in achievements:
        print("")
        print("Achievement unlocked: King of the wins")
        print("")
        achievements.append("King of the wins: win 50 times")
      updatesavedata(wins, money, losses, ties, achievements) #Update save data
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
        achievements = []
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
    print("")
    print("Techspark academy for inspiration")
    time.sleep(1)
    print("")
    print("Tested by Quadakr on github")
    print("")
    print("")
    time.sleep(1)
    print("Thanks for playing!")
    for i in range(3):
      print("")
  elif player_input == "a": #Show achievements
    print("You have: ")
    print("")
    print("\n".join(achievements))
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
