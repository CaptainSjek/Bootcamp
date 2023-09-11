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
# prompt om één letter in te geven. Alleen letters van het alfabet zijn acceptabel. Pas als de gebruiker precies één letter heeft ingegeven eindigt de functie, en de letter wordt dan als een hoofdletter geretourneerd.


def get_integer(a):
    a = input("Geef hier een integer. ")
    return a
print(int("a"))

def get_float(a):
    a = input("Geef hier een float. ")
    return a
print(float("a"))


#def getString():

#def get_letter():