# Opdracht 3: 
# Bereken met een while loop hoeveel keer 25 in 625 past.
# (Let op: max. 8 regels code!)

i = 25
getal = 1

while 625 >= i:
    i += 25
    getal += 1
    if i == 625:
        print(f"25 past {getal} keer in 625")   

