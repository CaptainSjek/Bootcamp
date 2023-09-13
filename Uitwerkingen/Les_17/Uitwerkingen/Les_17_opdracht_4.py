# Opdracht 4:
# Verslavend: de gebruikers vinden je game zo leuk dat ze er niet mee kunnen stoppen.
# Pas je game daarom als volgt aan: 
# - goed geraden? Vraag of de gebruiker nog een ronde wil spelen.
# - aan het einde print je het aantal gespeelde ronden en het aantal keer dat de gebruiker fout heeft geraden.
import random
from Raadspel import *
getal = random.randint(1,5)
doorgaan = True
levens = 3
rondes = 0
fout = 0
antwoord = "j, ja, y, yes"
nee = "N"


print(getal)
while doorgaan:
    try:
        inputgetal = int(input("Vul hier een getal in tussen de 1 en 5: "))
    except ValueError:
        print("Vul een legitiem getal in! ")
    if inputgetal == getal:
        print(f"\033[32mJe hebt het getal goed geraden!\033[0m")
        vraag = input("Wil je nog een keer spelen? Type J of N: ").lower()
        rondes += 1
        if vraag in antwoord:
            getal = random.randint(1, 5)
            levens = 3
        else:
            print("Bedankt voor het spelen, tot de volgende keer! ")
            doorgaan = False
    elif levens >= 1:
        levens -= 1
        fout += 1
        print("\033[31mHelaas! Je hebt het getal niet goed geraden. \033[0m")
        doorgaan = True

    if levens == 0:
        vraag = input("Oei, je levens zijn op! Wil je nog een keer spelen? Type J of N: ")
        if vraag in antwoord:
                raadspel()
                getal = random.randint(1,5)
                levens = 3
        else:
            print("Bedankt voor het spelen, tot de volgende keer! ")
            doorgaan = False
print(f"Je hebt {rondes} keer gespeeld en {fout} keer het verkeerde getal geraden. ")