# Opdracht 2:
# Oh ja: we (oefenen het) formatteren het ook nog even netjes:
# Is je cijfer 6 of groter dan print je:
# "Gefeliciteerd, {omschrijving} je resultaat is een {cijfer}"

# Heb je lager dan een 6 gescoord dan wordt het: 
# "Jammer, {omschrijving} je resultaat is een {cijfer}"

# Zorg ervoor dat een gebruiker een cijfer tussen 1 en 10 kan invoeren. 
# Wordt het getal te groot of te klein dan moet je een melding geven: 'Dit kan ik niet omzetten!'

cijfer = int(input("Type hier je cijfer "))

if cijfer == 1:
    omschrijving = "Zeer slecht"
elif cijfer == 2:
    omschrijving = "Slecht"
elif cijfer == 3:
    omschrijving = "Gering"
elif cijfer == 4:
    omschrijving = "Onvoldoende"
elif cijfer == 5:
    omschrijving = "Bijna Voldoende"
elif cijfer < 6:
    omschrijving = "Voldoende"
elif cijfer == 7:
    omschrijving = "Ruim voldoende"
elif cijfer == 8:
    omschrijving = "Goed"
elif cijfer == 9:
    omschrijving = "Zeer goed"
elif cijfer == 10:
    omschrijving = "Uitmuntend"
else:
    print("Dit kan ik niet omzetten! ")
if cijfer >= 6:
    print(f"Gefeliciteerd, {omschrijving} je resultaat is een {cijfer}")
if cijfer < 6:
    print(f"Jammer, {omschrijving} je resultaat is een {cijfer}")
