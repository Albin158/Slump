Namn = [
  "AlphonzeBronze",
  "Ubåt",
  "Ormben",
  "Farfars otroliga rullande das",
  "BullArne",
  "Roberto",
  "Råtthäst",
  "Final"
]

Efternamn = [
  "Karlsson pyssling",
  "fuff",
  "dumberg",
  "Tusk",
  "Fartdåre",
  "Lönneberga",
  "Barnspark",
  "Countdown"
]


import random

for i in range(0, 5):
  Namnval = random.randint(0, len(Namn)-1)
  Efternamnval = random.randint(0, len(Efternamn)-1)

  print(f"{Namn[Namnval].capitalize()}  {Efternamn[Efternamnval]}")