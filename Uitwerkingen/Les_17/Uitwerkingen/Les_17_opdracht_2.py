# Opdracht 2:
# Breid je programma nu zodanig uit dat de gebruiker net zolang moet raden tot hij het juiste getal heeft gevonden.


import random
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

# while doorgaan == True:
#     try:
#         inputgetal = input(int("Vul hier een getal in tussen de 1 en 5: "))
#         trueOrfalse = random.randint(0, 5)
#         if trueOrfalse == 5:
#             (print("\033[32mJe hebt het getal goed geraden! \033[0m"))
#             doorgaan == False
#         elif trueOrfalse == 0:
#             print("\033[31mJe hebt het getal niet goed geraden! \033[0m")

    # except ValueError:
    #     print("Vul een legitiem getal in! ")
        
        