# # # doorgaan = True


# # # while doorgaan:
# # #     try:
# # #         getal = int(input("voer een getal in"))
# # #         print(getal)
# # #         doorgaan == False
        
# # #     except ValueError:
# # #         print("Fout")
# # from MyFunctions import *
# import random
# from termcolor import colored
# getal1 = random.randint(1,5)
# getal_invullen = True
# while getal_invullen:
#     try:
#         raadgetal = int(input("raad een getal tussen 1 en 5 "))
#     except ValueError:
#         print("vul een getal in tussen 1 en 5! ")
#     if raadgetal == getal1:
#         print(colored("goed geraden", "green"))
#         getal_invullen = False
#     else:
#         print(colored("verkeerd geraden!", "red"))
#         getal_invullen = True



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
rondes = 1
fout = 0
nee = "N"
ja = "J"
print(getal)
while doorgaan:
    try:
        inputgetal = int(input("Vul hier een getal in tussen de 1 en 5: "))
    except ValueError:
        print("Vul een legitiem getal in! ")
        continue
    if inputgetal == getal:
        print(f"\033[32mJe hebt het getal goed geraden!\033[0m")
        doorgaan = False
        vraag = input("Wil je nog een keer spelen? Type J of N: ")
        rondes += 1
        if vraag == ja:
            raadspel()
        else:
            print("Bedankt voor het spelen")         
    else:
        levens -= 1
        fout += 1
        doorgaan = False
        print("\033[31mJe hebt het getal niet goed geraden! \033[0m")

    if levens == 0:
        doorgaan = False
print(f"Je hebt {rondes} keer gespeeld en {fout} keer het verkeerde getal geraden. ")
# if vraag == ja:
#     raadspel()