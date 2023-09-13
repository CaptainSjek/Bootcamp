# Opdracht 4:
# Verslavend: de gebruikers vinden je game zo leuk dat ze er niet mee kunnen stoppen.
# Pas je game daarom als volgt aan: 
# - goed geraden? Vraag of de gebruiker nog een ronde wil spelen.
# - aan het einde print je het aantal gespeelde ronden en het aantal keer dat de gebruiker fout heeft geraden.
import random
from Raadspel import *
getal = random.randint(1,5)
doorgaan = True
levens = 5
rondes = 0
fout = 1
# vraag = input("Type J of N: ")
nee = "N"
ja = "J"
while doorgaan:
    try:
        inputgetal = int(input("Vul hier een getal in tussen de 1 en 5: "))
    except ValueError:
        print("Vul een legitiem getal in! ")
    if inputgetal == getal:
        print(f"\033[32mJe hebt het getal goed geraden!\033[0m")
        doorgaan = False
        for i in range(2):
            vraag = input("Wil je nog een keer spelen? Type J of N: ")
            if vraag == ja:
                raadspel()
                while vraag >= 0:
                    rondes += 1
            else:
                print("Bedankt voor het spelen")
                while inputgetal != getal:
                    fout += 1
            print(f"Je hebt {rondes} keer gespeeld en {fout} keer het verkeerde getal geraden. ")            
    elif levens == 0:
        doorgaan = False
    else:
        levens -= 1 
        print("\033[31mJe hebt het getal niet goed geraden! \033[0m")
#        doorgaan = True
        fout += 1
print(f"Je hebt {rondes} keer gespeeld en {fout} keer het verkeerde getal geraden. ")
# if vraag == ja:
#     raadspel()