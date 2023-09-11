# # Opdracht 4:
# # Schrijf een programma dat een lege lijst maakt en vervolgens de gebruiker vraagt om 5 woorden in te voeren.
# # Gebruik de append functie om elk woord aan de lijst toe te voegen 
# # en gebruik vervolgens een for-lus om door elk woord in de lijst te itereren en print elk woord op een aparte regel.

woorden = []
#cijfers.append(input("vul hier 5 woorden in"))

for x in range(5):
    woord = (input("voer een woord in "))
    woorden.append(woord)
print("De ingevoerde woorden zijn. ")
for woord in woorden:
    print(woord)



# fruits = ["apple", "banana", "cherry"]
# for x in fruits:
#   print(x)