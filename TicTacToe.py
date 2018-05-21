# TicTacToe
# Martina Ahlswede
# Data Science (BHTB MIM 12 S18)
# Python Exercise
#
#

#  1 | 2 | 3
#  ---------
#  4 | 5 | 6
#  ---------
#  7 | 8 | 9

spielfeld = [[1,2,3],[4,5,6],[7,8,9]]
spieler = 2
eingabe ='0'
spielzug = 0
feldok = True


def spielfeld_ausgabe():
  print()
  print(" ", spielfeld[0][0], "|", spielfeld[0][1], "|", spielfeld[0][2])
  print("  ---------")
  print(" ", spielfeld[1][0], "|", spielfeld[1][1], "|", spielfeld[1][2])
  print("  ---------")
  print(" ", spielfeld[2][0], "|", spielfeld[2][1], "|", spielfeld[2][2])
  print()


#
# pruefe_eingabe() prueft auf Eingabe '1'..'9', 
# setzt das gewaehlte Feld auf 'X' oder 'O', wenn es nicht schon zuvor gesetzt war
#
def pruefe_eingabe():
  if (spieler == 1):
    feldok = True
    if (eingabe == "1" and spielfeld[0][0] == 1): spielfeld[0][0] = 'X'
    elif (eingabe == "2" and spielfeld[0][1] == 2): spielfeld[0][1] = 'X'
    elif (eingabe == "3" and spielfeld[0][2] == 3): spielfeld[0][2] = 'X'
    elif (eingabe == "4" and spielfeld[1][0] == 4): spielfeld[1][0] = 'X'
    elif (eingabe == "5" and spielfeld[1][1] == 5): spielfeld[1][1] = 'X'
    elif (eingabe == "6" and spielfeld[1][2] == 6): spielfeld[1][2] = 'X'
    elif (eingabe == "7" and spielfeld[2][0] == 7): spielfeld[2][0] = 'X'
    elif (eingabe == "8" and spielfeld[2][1] == 8): spielfeld[2][1] = 'X'
    elif (eingabe == "9" and spielfeld[2][2] == 9): spielfeld[2][2] = 'X'
    else: feldok = False
  elif (spieler == 2):
    feldok = True
    if (eingabe == "1" and spielfeld[0][0] == 1): spielfeld[0][0] = 'O'
    elif (eingabe == "2" and spielfeld[0][1] == 2): spielfeld[0][1] = 'O'
    elif (eingabe == "3" and spielfeld[0][2] == 3): spielfeld[0][2] = 'O'
    elif (eingabe == "4" and spielfeld[1][0] == 4): spielfeld[1][0] = 'O'
    elif (eingabe == "5" and spielfeld[1][1] == 5): spielfeld[1][1] = 'O'
    elif (eingabe == "6" and spielfeld[1][2] == 6): spielfeld[1][2] = 'O'
    elif (eingabe == "7" and spielfeld[2][0] == 7): spielfeld[2][0] = 'O'
    elif (eingabe == "8" and spielfeld[2][1] == 8): spielfeld[2][1] = 'O'
    elif (eingabe == "9" and spielfeld[2][2] == 9): spielfeld[2][2] = 'O'
    else: feldok = False
  return(feldok)


def pruefe3inreihe(cxo):
  spielergewonnen = False
  if (spielfeld[0][0] == cxo and spielfeld[0][1] == cxo and spielfeld[0][2] == cxo):
    spielergewonnen = True
  elif (spielfeld[1][0] == cxo and spielfeld[1][1] == cxo and spielfeld[1][2] == cxo):
    spielergewonnen = True
  elif (spielfeld[2][0] == cxo and spielfeld[2][1] == cxo and spielfeld[2][2] == cxo):
    spielergewonnen = True
  elif (spielfeld[0][0] == cxo and spielfeld[1][0] == cxo and spielfeld[2][0] == cxo):
    spielergewonnen = True
  elif (spielfeld[0][1] == cxo and spielfeld[1][1] == cxo and spielfeld[2][1] == cxo):
    spielergewonnen = True
  elif (spielfeld[0][2] == cxo and spielfeld[1][2] == cxo and spielfeld[2][2] == cxo):
    spielergewonnen = True
  elif (spielfeld[0][0] == cxo and spielfeld[1][1] == cxo and spielfeld[2][2] == cxo):
    spielergewonnen = True
  elif (spielfeld[0][2] == cxo and spielfeld[1][1] == cxo and spielfeld[2][0] == cxo):
    spielergewonnen = True
  return spielergewonnen

# main

spielfeld_ausgabe()

while spielzug < 9:

  if (spieler == 2):
    spieler = 1
    feldok = False
    while feldok == False:
      eingabe = input ("Spieler 1, welches Feld (1..9) ? ") 
      feldok = pruefe_eingabe()
      if feldok == False: print("Falsche Eingabe oder Feld belegt")
  elif (spieler == 1):
    spieler = 2
    feldok = False
    while feldok == False:
      eingabe = input ("Spieler 2, welches Feld (1..9) ? ")
      feldok = pruefe_eingabe()
      if feldok == False: print("Falsche Eingabe oder Feld belegt")

  
  spielfeld_ausgabe()

  if (pruefe3inreihe('X') == True):
    print("Spieler 1 gewinnt das Spiel")
    break

  if (pruefe3inreihe('O') == True):
    print("Spieler 2 gewinnt das Spiel")
    break

  spielzug+=1
  if (spielzug == 9):
    print("Unentschieden")

#end while
