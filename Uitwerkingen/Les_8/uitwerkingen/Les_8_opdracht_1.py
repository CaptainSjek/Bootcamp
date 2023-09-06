# Opdracht 1:
# In Nederland krijg je op school regelmatig een cijfer.
# Wist je dat bij die cijfers ook een omschrijving hoort? 
# Schrijf jij een programma wat de juiste omschrijving print bij een cijfer.

# Houd rekening met het volgende:
# Je schrijft een programma met 1 variabele: cijfer. Dit cijfer gebruik je om de omschrijving te printen:

# Cijfer	Omschrijving
# 10	uitmuntend
# 9	zeer goed
# 8	goed
# 7	ruim voldoende
# 6	voldoende
# 5	bijna voldoende
# 4	onvoldoende
# 3	gering
# 2	slecht
# 1	zeer slecht

cijfer = int(input("Type hier je cijfer "))


if cijfer == 1:
    print("Zeer slecht")
elif cijfer == 2:
    print("Slecht")
elif cijfer == 3:
    print("Gering")
elif cijfer == 4:
    print("Onvoldoende")
elif cijfer == 5:
    print("Bijna Voldoende")
elif cijfer == 6:
    print("Voldoende")
elif cijfer == 7:
    print("Ruim voldoende")
elif cijfer == 8:
    print("Goed")
elif cijfer == 9:
    print("Zeer goed")
elif cijfer == 10:
    print("Uitmuntend")
#elif cijfer == 0:
#    print("Sorry maar het is niet mogelijk om een 0 als cijfer te scoren")
#else:
#    print("Sorry maar het is niet mogelijk om een cijfer hoger dan 10 te scoren")