# Opdracht 5:
# Stel je hebt 10.000 euro bij de bank en krijgt daarop 2,8% rente per jaar.
# Hoeveel geld heb je na 5 jaar (als je er verder niets bijstort of afhaalt?)
# En na 15 jaar? (als je er niets afhaalt of bijstort?)

# geld = 10000
# rente = 0.028

# while geld == 10000:
#     print((geld * rente) + 10000)
#     geld =+ 15




geld= 10000
rente = 2.8
jaar = 0
while jaar < 15:
    jaar += 1

    geld += geld / 100 * rente
    print(f"Na {jaar} heb je €{round(geld)} op je rekening staan")

#Na 5 jaar heb je €11481 op je rekening staan
#Na 15 jaar heb je €15132 op je rekening staan
