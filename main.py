#imports
import os
import time
import colorama as cr
import math

cr.init(autoreset=True)


#clears the console every now and then
def clearConsole():
    command = 'clear'
    os.system(command)


#the actual code :noooooo: 

print(f"{cr.Fore.BLUE}This is mandatory") 
time.sleep(3)
clearConsole()

print("Loading main.py            {⬜         } 20%") #Loading
time.sleep(2)
clearConsole()
print("Loading main.py            {⬜⬜       } 40%") #Loading
time.sleep(2)
clearConsole()
print("Loading README.md          {⬜⬜⬜     } 60%") #Loading
time.sleep(0.4)
clearConsole()
print("Loading rep://files        {⬜⬜⬜⬜   } 80%") #Loading
time.sleep(2)
clearConsole()
print("Loading rep://files/images {⬜⬜⬜⬜   } 85%") #Loading
time.sleep(2)
clearConsole()
print("Loading rep://files/Saves  {⬜⬜⬜⬜   } 90%") #Loading
time.sleep(2)
clearConsole()
print("Loading rep://files/sounds {⬜⬜⬜⬜   } 95%") #Loading
time.sleep(2)
clearConsole()
print("Loading poetry.lock        {⬜⬜⬜⬜⬜} 97%") #Loading
time.sleep(2)
clearConsole()
print("Loading pyproject.toml     {⬜⬜⬜⬜⬜} 99%") #Loading
time.sleep(5)
clearConsole()
print("Loading Complete")
time.sleep(1.3)
clearConsole()

user = input(f"{cr.Fore.GREEN}USER? : ")
time.sleep(1)
clearConsole()

print(f"{cr.Fore.GREEN}Mysterious: Wake up " + user + ".")
time.sleep(0.5)
print(f"{cr.Fore.GREEN}Mysterious: You don't have enough time to waste.")

time.sleep(2)
print(f"{cr.Fore.LIGHTBLUE_EX}Respond With: | What | Where am I? |")

user_input1 = input(f"{cr.Fore.LIGHTRED_EX} " + user + " : ")

time.sleep(2)

if user_input1=="What":
    print(f"{cr.Fore.GREEN}Mysterious: Wait Did You Lose Your Memory?")

if user_input1=="Where am I?":
    print(f"{cr.Fore.GREEN}Mysterious: Wait Did You Lose Your Memory?")

if user_input1=="where am I?":
    print(f"{cr.Fore.GREEN}Mysterious: Wait Did You Lose Your Memory?")

if user_input1.lower() == "what" or user_input1.lower() == 'where am i?':
    print(f"{cr.Fore.GREEN}Mysterious: Wait Did You Lose Your Memory?")

else:
    print(f"{cr.Fore.RED}Game.Console: '" + user_input1 +"' Considered to be a input Error. Please restart game. :(")
    exit()
     

print(f"{cr.Fore.LIGHTBLUE_EX}Respond With: | No? | Maybe |")


user_input2 = input(f"{cr.Fore.LIGHTRED_EX} " + user + " : ")

if user_input2=="No?":
   print(f"{cr.Fore.GREEN}Mysterious: Sus")
   
if user_input2=="no?":
   print(f"{cr.Fore.GREEN}Mysterious: Sus")

  
if user_input2=="Maybe":
   print(f"{cr.Fore.GREEN}Mysterious: Sus")

if user_input2=="maybe":
   print(f"{cr.Fore.GREEN}Mysterious: Sus")

else:
    print(f"{cr.Fore.RED}Game.Console: '" + user_input2 +"' Considered to be a input Error. Please restart game. :(")

time.sleep(2)

print(f"{cr.Fore.GREEN}Mysterious: ...")

time.sleep(2)

print(f"{cr.Fore.GREEN}Mysterious: Oh I forgot, brainwashees don't do humour")
