def updatesavedata(wins, money, losses, ties):
  with open("save_data/money", "w") as h:
    h.write(str(money))
  with open("save_data/wins", "w") as h:
    h.write(str(wins))
  with open("save_data/losses", "w") as h:
    h.write(str(losses))
  with open("save_data/ties", "w") as h:
    h.write(str(ties))