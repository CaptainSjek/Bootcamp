#Opdracht: wat is het verschil tussen de 2

a=5
b=3
c=2
if (a==6 and b==4 or c==2):
    print("De conditie is waar")
else: 
    print("De conditie is niet waar")
    
a=5
b=3
c=2
if (a==6 and (b==4 or c==2)):
    print("De conditie is waar")
else:
    print("De conditie is niet waar")

#Commentaar: Omdat er haakjes staan veranderd de if statement