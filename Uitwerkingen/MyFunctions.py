# Opdracht 3:
# Je gaat een hulpmiddel schrijven die je bij het programmeren kunt gebruiken. 
# Maak de file: user_input.py.

# Hierin schrijf je de volgende functies:
# - get_integer()
# krijgt één string parameter, de prompt, en vraagt de gebruiker via
# die prompt om een integer in te geven. De functie retourneert een integer.


# - get_float() 
# krijgt één string parameter, de prompt, en vraagt de gebruiker via die
# prompt om een float in te geven. De functie retourneert een float.

# - getString() 
# krijgt één string parameter, de prompt, en vraagt de gebruiker via die
# prompt om een string in te geven. Alles wat de gebruiker ingeeft wordt als correct
# beschouwd. De functie retourneert de ingevoerde waarde als string.

# - get_letter() 
# krijgt één string parameter, de prompt, en vraagt de gebruiker via die
# prompt om één letter in te geven. Alleen letters van het alfabet zijn acceptabel.
# Pas als de gebruiker precies één letter heeft ingegeven eindigt de functie, en de letter wordt dan als een hoofdletter geretourneerd.


import random


#Functie Get Integer
def get_integer(prompt):
    while True:
        try:
            user_input = input(prompt)
            integer_value = int(user_input)
            return integer_value
        except ValueError:
            print("Ongeldige invoer.")

integer_input = get_integer("Voer een geheel getal in: ")
print("Ingevoerd geheel getal:", integer_input)


#Functie Get Float
def get_float(prompt):
    while True:
        try:
            user_input = input(prompt)
            float_value = float(user_input)
            return float_value
        except ValueError:
            print("Ongeldige invoer" )

float_input = get_float("Voer een komma getal in: ")
print("Ingevoerd komma getal: ", float_input)

#def getString():
def getString(prompt):
    while True:
        try:
            user_input = input(prompt)
            string_value = str(user_input)
            return string_value
        except ValueError:
            print("Ongeldige invoer" )

string_input = getString("Voer een woord/zin in: ")
print("Ingevoerd woord/zin: ", string_input)

#def get_letter():
def get_letter(prompt):
    user_input = input(prompt).lower()
    letter_value = (user_input)
    if user_input in ("a, b, c, d, e, f, g, h, i, j, k, l, m, n, o, p, q, r, s, t, u, v, w, x, y, z "):
            return letter_value.capitalize()
    else:
        print("Sorry maar deze letter ken ik niet")

letter_value = get_letter("Voer hier een letter in van het alfabet: ")
print("Ingevoerde letter:", letter_value)



