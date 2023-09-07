# Opdracht 3:
# Schrijf een programma met 3 variabelen:
# leeftijd = 18, snor = j (of n) en diploma = j (of n).

# Je schrijft een programma wat bepaalt of iemand is aangenomen. 
# Je bent aangenomen als je: 18 bent (of ouder) en een snor hebt of onder de 18 met een diploma.

# Let op:
# Je mag maar 1 if statement gebruiken!!!

# Test je programma door de variabelen te wijzigen.

leeftijd = int(input("Vul hier je leeftijd in. "))
snor = input("Heb je een snor? vul in J voor ja of N voor nee. ")
diploma = input("Heb je een diploma? Vul in J voor ja of N voor nee. ")

if leeftijd >= 18 and snor == "J" or leeftijd < 18 and diploma == "J":
    print("Gefeliciteerd je bent aangenomen.")
else:
    print("Sorry je bent helaas niet aangenomen.")