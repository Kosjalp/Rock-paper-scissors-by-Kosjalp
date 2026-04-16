import os
def updatesavedata(wins, money, losses, ties, achievements, purchases):
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
            h.write(f"{a}\n")
  with open("save_data/purchases", "w") as h:
    for p in purchases:
        h.write(f"{p}\n")

