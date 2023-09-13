# Opdracht 3:
# Zorg ervoor dat je drie rondjes achter elkaar kunt spelen en er dus drie keer een getal moet worden geraden.

#from Raadspel import raadspel
import random

getal = random.randint(1,5)
doorgaan = True
games = 3


while doorgaan:
    try:
        inputgetal = int(input("Vul hier een getal in tussen de 1 en 5: "))
    except ValueError:
        print("Vul een legitiem getal in! ")
#        inputgetal = int(input("Vul hier een getal in tussen de 1 en 5: "))
    if inputgetal == getal:
        (print("\033[32mJe hebt het getal goed geraden! \033[0m"))
        doorgaan = False
    elif games == 0:
        doorgaan = False
    else:
        games -= 1 
        print("\033[31mJe hebt het getal niet goed geraden! \033[0m")
        doorgaan = True
    
    

# for i in range(3):
#     print(raadspel)
