# Opdracht 4:
# Verslavend: de gebruikers vinden je game zo leuk dat ze er niet mee kunnen stoppen.
# Pas je game daarom als volgt aan: 
# - goed geraden? Vraag of de gebruiker nog een ronde wil spelen.
# - aan het einde print je het aantal gespeelde ronden en het aantal keer dat de gebruiker fout heeft geraden.
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
vraag = input("Vond je dit spel leuk? Type Ja om nog een keer te spelen: ")
if vraag == "Ja":
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