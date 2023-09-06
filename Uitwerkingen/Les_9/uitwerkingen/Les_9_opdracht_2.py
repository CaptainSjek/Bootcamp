# Opdracht 2:
# De modulo kun je gebruiken om te controleren wat het restant is na een deling met als resultaat een heel getal. 
# Bijv. 	9%2 = 1
# 	9%5 = 4

# Schrijf een programma wat controleert of een getal (zonder rest) deelbaar is door 7 en 11.
# De ene keer print je: "Dit getal is zonder rest deelbaar door 7 en 11"
# De andere keer: "Dit getal is niet zonder rest deelbaar door 7 en 11"

# Test je programma eens met: 77. (en uiteraard nog met wat andere getallen.) 	  

getal = 77



if getal % 7 == 0 or 11 == 0:
    print("Dit getal is zonder rest deelbaar door 7 en 11")
else:
    print("Dit getal is niet zonder rest deelbaar door 7 en 11")