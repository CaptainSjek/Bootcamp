# Opdracht 1:
# je spel (van de vorige les) wordt een hit.
# Gebruikers klagen alleen dat het erg lang duurt voordat ze klaar zijn met raden.
# Na diepgravend onderzoek kom er achter dat je nergens meldt in welke range men kan raden en gebruikers blijken dus te denken dat ze tussen 1 en 100 mogen raden.

# Breid je gereedschap uit met een functie die kan controleren of de ingevoerde waarde in een lijst voorkomt. 
# Je kunt deze functie op twee plaatsen inzetten. Waar? En doe dit dan ook.

import random               #Zorgt ervoor dat getallen door de computer gerandomized kunnen worden
from Raadspel import *      #Zorgt ervoor dat de functie gebruikt kan worden
getal = random.randint(1,5) #Variabele getal zorgt voor een willekeurig getal 1,2,3,4 of 5
doorgaan = True             #Variabele zorgt ervoor dat het spel stopt of doorgaat
levens = 3                  #3 levens, ook wel pogingen om het getal te raden
rondes = 0                  #Telt de rondes bij elkaar op hoeveel er gespeeld is
fout = 0                    #Telt de fout gegokte keuzes bij elkaar op
antwoord = "j, ja, y, yes"  #Input of de gebruiker door wilt spelen
#nee = "N"


print(getal)
while doorgaan:                                                                 #
    try:                                                                        # Hier vraagt de computer de speler om een getal tussen de 1 en 5 te kiezen
        inputgetal = int(input("Vul hier een getal in tussen de 1 en 5: "))     # Als de gebruiker geen 
        if inputgetal > 5:
            raise ValueError
        
    except ValueError:                                                          #
        print("\033[31mDit getal is hoger dan 5! Dit kost je een leven :-(\033[0m ")           #
    if inputgetal == getal:                                                     #
        print(f"\033[32mJe hebt het getal goed geraden! \033[0m")                #
        vraag = input("Wil je nog een keer spelen? Type J of N: ").lower()      #
        rondes += 1                                                             #
        if vraag in antwoord:                                                   #
            getal = random.randint(1, 5)                                        #
            levens = 3                                                          #
        else:                                                                   #
            print("Bedankt voor het spelen, tot de volgende keer! ")            #
            doorgaan = False                                                    #
    elif levens >= 1:                                                           #
        levens -= 1                                                             #
        fout += 1                                                               #
        print("\033[31mHelaas! Je hebt het getal niet goed geraden. \033[0m")   #
        doorgaan = True                                                         #

    if levens == 0:
        vraag = input("Oei, je levens zijn op! Wil je nog een keer spelen? Type J of N: ").lower()
        if vraag in antwoord:
                raadspel()
                getal = random.randint(1,5)
                levens = 3
        else:
            print("Bedankt voor het spelen, tot de volgende keer! ")
            doorgaan = False
print(f"Je hebt {rondes} keer gespeeld en {fout} keer het verkeerde getal geraden. ")