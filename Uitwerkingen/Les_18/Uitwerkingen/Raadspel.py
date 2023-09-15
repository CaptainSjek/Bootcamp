import random

def raadspel():
    getal = random.randint(1,5)
    doorgaan = True


    while doorgaan:
        try:
            inputgetal = int(input("Vul hier een getal in tussen de 1 en 5: "))
        except ValueError:
            print("Vul een legitiem getal in! ")
            inputgetal = int(input("Vul hier een getal in tussen de 1 en 5: "))
        if inputgetal == getal:
            (print("\033[32mJe hebt het getal goed geraden! \033[0m"))
            doorgaan = False
        else:
            print("\033[31mJe hebt het getal niet goed geraden! \033[0m")
            doorgaan = True

def rangecheck(inputgetal):
    if inputgetal > 5:
            raise ValueError 



def raadspel2():
    while doorgaan:                                                                 #
        try:                                                                        # Hier vraagt de computer de speler om een getal tussen de 1 en 5 te kiezen
            inputgetal = int(input("Vul hier een getal in tussen de 1 en 5: "))     # Als de gebruiker geen 
            # if inputgetal > 5:
            #     raise ValueError        
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
            doorgaan = True 