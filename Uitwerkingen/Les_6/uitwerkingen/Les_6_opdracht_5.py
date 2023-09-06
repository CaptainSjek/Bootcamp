# Opdracht 5 (hard):
# Voer opdracht 2 nogmaals uit maar nu met 3 variabelen: a, b en c.
# Hint: je kunt dit in twee stappen uitvoeren.
# Vervolgens zorg je er ook weer voor dat de gebruiker de getallen kan invoeren.

# a = int(input("Vul hier leeftijd A in."))
# b = int(input("Vul hier leeftijd B in."))

# if (a > b):
#     print(f"variabele a is het grootst want {a} is groter dan {b}")
# if (b > a):
#     print(f"variabele b is het grootst want {b} is groter dan {a}")
# if (a == b):
#     print("variabele a en b zijn gelijk.")

a = int(input("Vul hier leeftijd A in. "))
b = int(input("Vul hier leeftijd B in. "))
c = int(input("Vul hier leeftijd C in. "))

if a > b and a > c:
    print(f"variabele A is het grootst want {a} is groter dan {b} en groter dan {c}")
elif b > a and b > c:
    print(f"variabele B is het grootst want {b} is groter dan {a} en groter dan {a}")
elif c > a and c > b:
    print(f"variabele C is het grootst want {c} is groter dan {a} en groter dan {b}")
else:
    print(f"Variabele A, B en C zijn allemaal gelijk") 
   

