#header
#add clear
import random as rnd
import os,time
from getpass import getpass as inputp
print("Rock, Paper, Scissors")
print(" v3.7, by cristian")
print("#####################")
print("")
def org(t):
  time.sleep(t)
  os.system("clear")
 
#rules
print("the only rule is, when one player is choosing, the other must look away.")
print("")

#variables
rn = (int(input("hom many times you wanna play?: "))) + 1
org(0)
against = input("do you wanna play against the computer, rather than someone else?: ").lower()
org(0)
ext = 0
sco = 0
sct = 0

for  i in range(1, rn):

 #input
 if against == "yes":
   plo = int(inputp("player one, choose; rock = 1, paper = 2, scissors = 3"))
   org(0.7)
   plt = rnd.randint(1, 3)
   org(0.7)
 else:
   plo = int(inputp("player one, choose; rock = 1, paper = 2, scissors = 3"))
   org(0.7)
   plt = int(inputp("player two, choose; rock = 1, paper = 2, scissors = 3"))
   print("")
   org(2)
 #brainzz
 if plo == 1:
   if plt == 1:
     print("both players choose rock, its a tie!")
     org(3)
   elif plt == 2:
     print("player two's paper covers player one's rock.")
     print("player 2 wins!")
     org(3)
     sct = sct + 1
   elif plt == 3:
     
     print("player one's rock smash player two's scissors!")
     print("player one wins!")
     org(3)
     sco = sco + 1
   else:
     print("player 2, your input is not one of the expected.")
     org(3)
 elif plo == 2:
    if plt == 1:
      print("player one's paper covers player two's rock.")
      print("player one wins!")
      org(3)
      sco = sco + 1
    elif plt == 2:
     print("both players choose paper, its a tie!")
     org(3)
    elif plt == 3:
     print("player two's scissors cut player one's paper!")
     print("player two wins!")
     org(3)
     sct = sct + 1
    else:
     print("player 2, your input is not one of the expected.")
     org(3)
 elif plo == 3:
   if plt == 1:
      print("player two's rock smash player one's scissors.")
      print("player two wins!")
      org(3)
      sct = sct + 1
   elif plt == 2:
     print("player one's scissors chop up player two's paper!")
     print("player one wins!")
     org(3)
     sco = sco + 1
   elif plt == 3:
     print("both player choose rock!, its a tie!")
     org(3)
   else:
     print("player 2, your input is not one of the expected.")
     org(3)
 else:
   print("player one, your input is not one of the expected")
   org(3)
 ext = ext + 1
if ext <= 3:
   print("round", ext, "fight!") 
else:
  org(3)
  print("results are:")
  print("")
  print("player one scored",sco,"points.")
  print("player two scored", sct, "points")
  org(4)
  if sco > sct:
    print("player one won!!")
    print("congrats")
  elif sco < sct:
    print("player two won!!")
    print("congrats")
  elif sco == sct:
    print("its a tie!!")
    print("both won!!")
  else:
    print("thats not even suposed to appear so uhh..")