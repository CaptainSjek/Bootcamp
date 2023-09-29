# doorgaan = True

# # while doorgaan:
# #     try:
# #         cijfer not in range(0,10):
# #         print(cijfer)
# #     if cijfer in range(0,10):
# #         break
# while doorgaan:                                                                 
#         try:                                                                        
#             cijfer = int(input("Voer hier een willekeurig getal in: "))
#             if cijfer > 10:
#              raise ValueError        
#         except ValueError:                                                          
#             print("\033[31mDit getal is te hoog probeer het nog eens! \033[0m ")
#         if cijfer <= 10:                                                     
#             print(f"\033[32mJe hebt het getal goed geraden! \033[0m")
#             break
MAX = 20
getal = int(input("Voer een getal in: "))
if getal > MAX:
   input(f"Het getal is groter dan {MAX}")
elif getal < MAX:
  input(f"Het getal is kleiner dan {MAX}")
else:
   input(f"Het getal is gelijk aan {MAX}")

def som_functie(a, b, c):
    totaal = a + b + c
    return totaal

getal1 = 200
getal2 = 5
getal3 = 12
antwoord = som_functie(getal1, getal2, getal3)# of de naam van je eigen functie.
print(f"De som van {getal1} + {getal2} + {getal3} = {antwoord}")