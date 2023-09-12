# Opdracht 5.

# Joris de Tester heeft het probleem opgelost. Helaas heeft hij wel weer een volgende uitdaging: 
# Gevraagd is tussen input en print 3 keer te printen: 
# "Een moment geduld a.u.b., de scherpste prijs wordt berekend."
# Voor het effect wacht het programma steeds een seconde.

# Joris is aan de slag gegaan en heeft de volgende code opgeleverd:

from time import sleep # je hoeft nog niet te weten wat een import is, Kopieer deze regel en je kunt je programma laten wachten met de opdracht sleep(x seconden)


oppervlakte = int(input('Hoeveel m2 vloerbedekking heeft u nodig? '))
prijs_m2 = 40


for i in range(5):
    print("Een moment geduld a.u.b., de scherpste prijs wordt berekend.")
    sleep(1)




# print("Een moment geduld a.u.b., de scherpste prijs wordt berekend.")
# sleep(1)
# print("Een moment geduld a.u.b., de scherpste prijs wordt berekend.")
# sleep(1)
# print("Een moment geduld a.u.b., de scherpste prijs wordt berekend.")
# sleep(1)

# secret code containing the answer of question 2

# end of secret

totaal = prijs_m2 * oppervlakte

print(f'Het scherpste prijs voor een oppervlakte van {oppervlakte} m2 is: Eur ' + str(totaal))

# Na onderzoek blijkt het echter effectiever te zijn om het aantal meldingen (plus sleeps) te vergroten naar 5.

# De opdracht aan jou is: schrijf een versie van het programma die een constante gebruikt voor het aantal te tonen meldingen.

