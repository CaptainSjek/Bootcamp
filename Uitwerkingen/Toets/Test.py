getal = (0,1,2,3,4,5,6,7,8,9,10)
doorgaan = True

# while doorgaan:
#     try:
#         cijfer not in range(0,10):
#         print(cijfer)
#     if cijfer in range(0,10):
#         break
while doorgaan:                                                                 
        try:                                                                        
            cijfer = int(input("Voer hier een willekeurig getal in: "))
            if cijfer > 10:
             raise ValueError        
        except ValueError:                                                          
            print("\033[31mDit getal is te hoog probeer het nog eens! \033[0m ")
        if cijfer == getal:                                                     
            print(f"\033[32mJe hebt het getal goed geraden! \033[0m")               