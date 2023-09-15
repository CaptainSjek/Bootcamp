# Cijfers voor proefwerken en tentamens vallen tussen nul en 10 (inclusief nul en 10), en worden altijd afgerond op halve punten.
# De Amerikaanse stijl van beoordelen gebruikt letters.
# Ter vergelijking,de cijfers 8.5 tot en met 10 zijn in Amerika “A,” 7.5 en 8 zijn “B," 6.5 en 7 zijn “C,” 5.5 en 6 zijn “D,” en 5 en lager is “F.”
# Schrijf code die deze vertaling van cijfers naar letters maakt, waarbij de gebruiker gevraagd wordt om het cijfer in te geven.
#  Als de gebruiker een cijfer buiten het gegeven bereik ingeeft, moet je een foutmelding geven.

cijfer = float(input("Vul hier je cijfer in: "))
A = range(8.5,10)
B = range(7.5,8)
C = range(6.5,7)
D = range(5.5,6)
f = range(0,5)




if cijfer in A:
    print("In Amerika zou je een A hebben. ")
elif cijfer in B:
    print("In Amerika zou je een B hebben. ")
elif cijfer in C:
    print("In Amerika zou je een C hebben. ")
elif cijfer in D:
    print("In Amerika zou je een D hebben. ")
else:
    print("In Amerika zou je een F hebben. ")