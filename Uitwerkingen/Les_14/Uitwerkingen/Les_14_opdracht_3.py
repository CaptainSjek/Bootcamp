# Opdracht 3:
# Schrijf een programma dat een lijst van fruitsoorten maakt en vervolgens de gebruiker vraagt om een fruitsoort in te voeren. 
# Gebruik de remove functie om het opgegeven fruit uit de lijst te verwijderen en print vervolgens de bijgewerkte lijst.

fruit = ["appel" , "banaan" , "mandarijn" , "kiwi" , "ananas" , "peer" , "citroen" , "limoen" ]
fruitsoort = input("Noem een fruitsoort. ")
answer = fruitsoort.lower()
fruit.remove(answer)
print(fruit)