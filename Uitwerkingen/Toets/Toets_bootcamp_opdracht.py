# Opdracht 1 (schrijf je antwoord als commentaar in een py file):


# a: Waarom is Visual Studio Code handiger voor software development dan bijvoorbeeld Notepad (kladblok)? Noem de voordelen!
# Voordeel: Visual Studio Code heeft extensies om zo het programmeren makkelijker te maken.
# Voordeel: Door middel van kleuren instellingen heb je beter overzicht over je code.
#
# b: Waarom is het goed dat je de commits van jouw code pusht naar github.com?
# Antwoord: Zodat je bij een eventuele grote fout terug kan gaan naar een vorige versie
# Antwoord: Je kan makkelijk je files pullen naar een andere computer

# Opdracht 2
# Maak het commentaar af.
a = 5  # dit is een voorbeeld van het datatype: Integer
b = 10.5 # dit is een voorbeeld van het datatype: Float
c = "Hallo wereld" # dit is een voorbeeld van het datatype: String

# Opdracht 3
# Schrijf code die de waarden van a en b omwisselt. Gebruik daarvoor een extra variabele.
a = 5
b = 10
# voeg jouw code toe…
# Controleer met onderstaande code of de waarden correct zijn verwisseld
print(f"a = {b}, b = {a}") # Moet "a = 10 b = 5" printen

# Opdracht 4:
# Los de problemen op (zonder exception handling).
leeftijd = int(input("Hoe oud ben je?"))
som = 67 - leeftijd
print(f"Dan duurt het nog ongeveer {som} jaar voordat je met pensioen mag!")
# Is 18 ingevuld? Dan zie je op de terminal: Dan duurt het nog ongeveer 49 jaar voordat je met pensioen mag!

#Opdracht 5: 
# Schrijf een functie die 3 getallen bij elkaar optelt en zorg ervoor
# dat de uitkomst ervan wordt getoond in de print
def som_functie(a, b, c):
    totaal = a + b + c
    return totaal

getal1 = 200
getal2 = 5
getal3 = 12
antwoord = som_functie(getal1, getal2, getal3)# of de naam van je eigen functie.
print(f"De som van {getal1} + {getal2} + {getal3} = {antwoord}")

#Opdracht 6:
# Maak de volgende code af:# Je moet bijbetalen als je over je minuten of je GB's heen gaat en geen onbeperkt abonnement hebt.
AANTAL_GB = 20 # Aantal GB data in je bundel
AANTAL_MINUTEN = 200 # Aantal belminuten in je bundel
ONBEPERKT = False # test ook met True
aantal_minuten_gebeld = int(input("Hoeveel minuten heb je gebeld?"))
aantal_GB_internet = int(input("Hoeveel GB's heb je gebruikt?"))
if aantal_GB_internet > AANTAL_GB or aantal_minuten_gebeld > AANTAL_MINUTEN:
    print("Let op: je moet bijbetalen!")
else:
    print("Niet aan de hand gebruik je mobiel lekker verder!")

#Opdracht 7:
# Print onder elkaar de getallen 1-250 met max 2 regels code.
for i in range(250):
    i+=0

#Opdracht 8:
# Gegeven is:
lijst_eten = ['appel', 'pannenkoek', 'kiwi', 'broodjehamburger']

#Opdracht A
print("Onze Menukaart:")
print("Appel")
print("Pannenkoek")
print("Kiwi")
print("Hamburger")

# Opdracht B
max_lengte = -1
for lengte in lijst_eten:
    if len(lengte) > max_lengte:
        max_lengte = len(lengte)
        antwoord = lengte
 
print(f"Het langste woord is :  {antwoord}")

# Opdracht 9:
# Schrijf een programma wat de gebruiker vraagt een cijfer in te voeren via de terminal.
# Dit blijf je herhalen totdat de gebruiker een getal tussen 0 en 10 heeft ingevoerd.
# Voert de gebruiker iets anders in dan een getal: geef een foutmelding.

doorgaan = True

while doorgaan:                                                                 
        try:                                                                        
            cijfer = int(input("Voer hier een willekeurig getal in: "))
            if cijfer > 10:
             raise ValueError        
        except ValueError:                                                          
            print("\033[31mDit getal is te hoog probeer het nog eens! \033[0m ")
        if cijfer <= 10:                                                     
            print(f"\033[32mJe hebt het getal goed geraden! \033[0m")
            break

#Opdracht 10:
# repareer de volgende code:
MAX = 20
getal = int(input("Voer een getal in: "))
if getal > MAX:
   input(f"Het getal is groter dan {MAX}")
elif getal < MAX:
  input(f"Het getal is kleiner dan {MAX}")
else:
   input(f"Het getal is gelijk aan {MAX}")