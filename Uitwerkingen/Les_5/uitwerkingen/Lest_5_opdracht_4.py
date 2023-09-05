#Schrijf code die de oppervlakte van een cirkel berekent, gebruik makend
#van variabelen straal en pi = 3.14159. Voor het geval je het vergeten bent, de formule is
#straal keer straal keer pi. 
#Toon de uitkomst als volgt: “De oppervlakte van een cirkel met straal ... is ...”
pi = 3.14159


straal = int(input("vul hier de straal in "))

#Dit is hoe ik het eerst deed
#print("de oppervlakte van een cirkel met straal" , straal , " is " , straal *  straal * pi)
#print("de omtrek van een cirkel met straal" , straal , " is " , pi * (straal * 2))

#door middel van formating
print(f"de oppervlakte van een cirkel met straal {straal} is {straal *  straal * pi}")
print(f"de omtrek van een cirkel met straal {straal} is {pi * straal * 2}")


