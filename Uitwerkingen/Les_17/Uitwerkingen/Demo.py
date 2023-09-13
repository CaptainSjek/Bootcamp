# # doorgaan = True


# # while doorgaan:
# #     try:
# #         getal = int(input("voer een getal in"))
# #         print(getal)
# #         doorgaan == False
        
# #     except ValueError:
# #         print("Fout")
# from MyFunctions import *
import random
from termcolor import colored
getal1 = random.randint(1,5)
getal_invullen = True
while getal_invullen:
    try:
        raadgetal = int(input("raad een getal tussen 1 en 5 "))
    except ValueError:
        print("vul een getal in tussen 1 en 5! ")
    if raadgetal == getal1:
        print(colored("goed geraden", "green"))
        getal_invullen = False
    else:
        print(colored("verkeerd geraden!", "red"))
        getal_invullen = True