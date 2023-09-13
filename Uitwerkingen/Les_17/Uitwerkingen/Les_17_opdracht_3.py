# Opdracht 3:
# Zorg ervoor dat je drie rondjes achter elkaar kunt spelen en er dus drie keer een getal moet worden geraden.

#from Raadspel import raadspel
from Raadspel import *
import random

getal = random.randint(1,5)
doorgaan = True
games = 3
nee = "N"
ja = "J"

while doorgaan:
    try:
        inputgetal = int(input("Vul hier een getal in tussen de 1 en 5: "))
    except ValueError:
        print("Vul een legitiem getal in! ")
    if inputgetal == getal:
        (print("\033[32mJe hebt het getal goed geraden! \033[0m"))
        doorgaan = False
        for i in range(3):
            vraag = input("Wil je nog een keer spelen? Type J of N: ")
            if vraag == ja:
                raadspel()
            else:
                print("Bedankt voor het spelen")        
    elif games == 0:
        doorgaan = False
    else:
        games -= 1 
        print("\033[31mJe hebt het getal niet goed geraden! \033[0m")
        doorgaan = True
    
    

# for i in range(3):
#     print(raadspel)
