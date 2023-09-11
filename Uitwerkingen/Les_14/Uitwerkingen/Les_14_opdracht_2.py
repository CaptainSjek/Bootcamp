# Opdracht 2:
# Schrijf een programma dat een lijst van 5 getallen maakt en vervolgens de gebruiker vraagt om een index in te voeren. 
# Gebruik de pop functie om het getal op de opgegeven index uit de lijst te verwijderen en print vervolgens het verwijderde getal en de bijgewerkte lijst.

cijfers = ["0" ,"1" , "2" , "3" , "4" , "5"]
input = input("Geef een cijfer onder de 6. ")
cijfers.pop(int(input))
print(cijfers)
