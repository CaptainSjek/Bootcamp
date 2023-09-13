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