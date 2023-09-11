# Opdracht 1:
# Maak een tuple met een lijst kleuren.
# Schrijf code die de gebruiker vraagt om hun naam en favoriete kleur. 
# Controleer of de favoriete kleur van de gebruiker in de tuple voorkomt. 

# Is dat het geval: print klein verhaaltje met daarin de naam naam en kleur.
# #Anders print je: "Deze kleur is niet zo geweldig!"

mytuple = ("Rood" , "Groen" , "Blauw" , "Geel" , "Paars")
naam = input("Wat is jouw naam? ")
answer = input("Wat is jouw favoriete kleur? ")


if answer in mytuple:
    print(f"Hoi {naam}, ik vind {answer} ook een mooie kleur! ")
else:
    print("Deze kleur is niet zo geweldig! ")