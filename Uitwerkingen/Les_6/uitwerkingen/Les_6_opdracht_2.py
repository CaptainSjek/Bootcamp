#Schrijf een programma met twee variabelen: 
# - a = 3
# - b = 7
#Bepaal met behulp van code welke variabele het hoogste getal is. 
#Je laat je programma kiezen welke van de drie meldingen moeten worden gestuurd:
#"Variabele a is het grootst want {waarde a} is groter dan {waarde b}"
#"Variabele b is het grootst want {waarde b} is groter dan {waarde a}"
#"Variabele a en b zijn gelijk."
#Test je programma door a en b een paar keer een andere waarde te geven.
#Als laatste stap laat je de gebruiker de getallen a en b invoeren. Zorg ervoor dat je programma goed blijft werken.

a = int(input("Vul hier leeftijd A in."))
b = int(input("Vul hier leeftijd B in."))

if (a > b):
    print(f"variabele a is het grootst want {a} is groter dan {b}")
if (b > a):
    print(f"variabele b is het grootst want {b} is groter dan {a}")
if (a == b):
    print("variabele a en b zijn gelijk.")