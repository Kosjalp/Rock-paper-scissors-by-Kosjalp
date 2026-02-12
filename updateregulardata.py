import os
def updateregulardata():
    money = 0
    wins = 0
    losses = 0
    ties = 0
    achievements = []
    if os.path.exists("save_data/money"):
      with open("save_data/money", "r") as h:
        money = int(h.read())
    if os.path.exists("save_data/wins"):
      with open("save_data/wins", "r") as h:
        wins = int(h.read())
    if os.path.exists("save_data/losses"):
      with open("save_data/losses", "r") as h:
        losses = int(h.read())
    if os.path.exists("save_data/ties"):
      with open("save_data/ties", "r") as h:
        ties = int(h.read())
    if os.path.exists("save_data/achievements"):
      with open("save_data/achievements", "r") as h:
        achievements = [line.strip() for line in h if line.strip()]
    return money, wins, losses, ties, achievements
