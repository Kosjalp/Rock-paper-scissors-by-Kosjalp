import os
def updatesavedata(wins, money, losses, ties, achievements):
  os.makedirs("save_data", exist_ok=True)
  with open("save_data/money", "w") as h:
    h.write(str(money))
  with open("save_data/wins", "w") as h:
    h.write(str(wins))
  with open("save_data/losses", "w") as h:
    h.write(str(losses))
  with open("save_data/ties", "w") as h:
    h.write(str(ties))
  with open("save_data/achievements", "w") as h:
    for a in achievements:
        if isinstance(a, list):
            h.write(f"{a}\n")
        else:
            h.write(f"{a}\n")
