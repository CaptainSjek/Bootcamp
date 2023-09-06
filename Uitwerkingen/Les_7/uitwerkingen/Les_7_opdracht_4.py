# Opdracht 4:
# Neem je programma van opdracht 3. 
# Gebruik het nu om uit te rekenen hoeveel keer 12 in 625 past.
# Moest je hier nog iets voor aanpassen (behalve dan wat cijfers)? 
# (Let op: ook dit kan in max. 8 regels code!)


#In het programma van de vorige opdracht gebruikte ik optellen, helaas kwam ik daar met variabele 12 niet uit dus ik heb aftrekken gebruikt
i = 12
getal = 625
aantal_keer = 0
while getal >= i:
     getal -= i
     aantal_keer += 1
print("12 past", aantal_keer, "keer in 625, en er blijft", getal, "over.")
