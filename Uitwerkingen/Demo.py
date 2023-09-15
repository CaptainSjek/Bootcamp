# #naam = "Tim"
# #naam = naam + " " "den" " " "Hartog"

# naam = input("Voer hier je naam in ")
# achternaam = input("Voer hier je achternaam in ")
# volledigeNaam = naam + " " + achternaam
# print(volledigeNaam)
from termcolor import colored

# print(colored("Je hebt het getal niet goed geraden!", "red"))
# colored("TEXT", "COLOR") 

import random
raden = True
getal = random.randint(1, 5)
kansen = 2
uitslag1 = 0
uitslag2 = 0
respond1 = ["ja", "j"]
while raden == True:
    try:
        user_input = int(input("Raad het getal "))
        print(user_input)
    except ValueError:
        print("Voer een nummer in joh")
        user_input = int(input("Raad het getal "))
        raden = True
    if user_input == getal:
        print(colored("Goed geraden: " "Je hebt het getal goed geraden!", "green"))
        raden = True
        opnieuw = str(input("Wilt u opnieuw proberen? J/N "))
        uitslag2 += 1
        if opnieuw in respond1:
            getal = random.randint(1, 5)
            print("Veel succes")
            kansen = 2
        else:
            print(f"U heeft {uitslag1} keer verloren uit de {uitslag2} keren")
    elif kansen == 0:
        raden = False
        print("Helaas, je hebt veloren!")
        opnieuw = str(input("Wilt u opnieuw proberen? J/N "))
        if opnieuw in respond1:
            getal = random.randint(1, 5)
            print("Veel succes")
            kansen = 2
        uitslag1 += 1
    elif user_input != getal:
        kansen -= 1
        print(colored("Je hebt het getal niet goed geraden!", "red"))