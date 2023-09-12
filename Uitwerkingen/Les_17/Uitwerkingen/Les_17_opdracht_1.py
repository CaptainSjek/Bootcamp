# Opdracht 1:
# Raad het getal.
# Je gaat een eenvoudig raadspelletje maken. Hiervoor volg je een aantal stappen.
# 1. Maak een variabele aan en vul deze met een random getal tussen 1 en 5.
# 2. Vraag de gebruiker een getal in te voeren tussen 1 en 5.
# 3  a. Goed geraden: print dan in het groen: "Je hebt het getal goed geraden!"
#    b. Niet goed: print dan in het rood: "Je hebt het getal niet goed geraden!"
import random
from colorama import Fore
getal = (0,6)
inputgetal = input("Vul hier een getal in tussen de 1 en 6: ")
trueOrfalse = random.randint(0, 1)

if trueOrfalse == 1:
    print(\033[92m"Je hebt het goed geraden!"\033[0m)