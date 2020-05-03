
Meny = True # Här skapar jag ett variable som har ett värde på True eller boolean. Denna variable behövs i vårt while loop. 
option = 0    #  Ett annat variable som har värde 0. 
print("Hej och Välkommen! ")  # Den här meddalandet skrivs när programmet startas.
print("Du har fyra val!")  ## Den här meddalandet skrivs när programmet startas.
while Meny:   # While loopet körs direkt eller så länge Meny är true den körs. 
    # Nedan rad tillhör till while loopet och hr använder våran option varilable som är lika med en input och input i sin tur innehåller fyra stycken dictionarypygame.
    # Inne i input ges också information om vad användaren har för val. 
    option = input('''
Lexikon Engelska till Engelska [1] 
Vill du kolla upp alla ord i lexikon med dessa betydelse [2]
Saknas ord i lexikon skriv till oss [3]
Vill du avsluta programmet [4]
Ditt Val:''')
    if option > "4": # Här har vi en vilkor satts. Om användare skriver ett tal som är större än 4 då får de information att välja ett tal mellan 1 till 4.
        print("Du måste välja ett tal mellan 1 och 4!\n ") # \n ger ett rad space till den nedre raden. 

    elif option == "1":  # Här om option är lika med 1 då får man tillgång till ett Engleska lexikon. 
        import json # Vi laddar json modulen för att kunna använda våran data som vi har. Vårna data är json fil format. Denna modul är mycket användarbart för våran programpygame.
        # Våran data är baserad på key and value. Man skriver ett Ord (Key) och sen man får dess Betydelse (Value) som vran lexikon är baserad på. 
        from difflib import get_close_matches
        print("Welcome to longman dictionary!")
        mydata = json.load(open("data.json"))
        
        def translate(vocabulary):
            vocabulary = vocabulary.lower()
            if vocabulary in mydata:
                return mydata[vocabulary]
            elif len(get_close_matches(vocabulary, mydata.keys())) > 0:
                yn = input("Did you mean %s instead? Enter Y if yes, or N if no: " % get_close_matches(vocabulary, mydata.keys())[0])
                if yn == "Y":
                    return mydata[get_close_matches(vocabulary, mydata.keys())[0]]
                elif yn == "N":
                    return "the vocabulary may not exit in dictionary or dubble check the word."
                else:
                    return " We did not understand your word"
            else:
                 return "the vocabulary may not exit in dictionary or dubble check the word."
        vocabulary = input("Enter an English word:  ")
        print(translate(vocabulary))
        Meny = False

    elif option == "2":
        import json
        mydata = json.load(open("data.json"))
        print(mydata)
        Meny = False
                   
    elif option == "3":
        import os
        nyord = input("Skriv ditt nya ord!  ")
        print("Ditt nya ord sparas i en fil! ")
        filename = input("Vad ska hetta filen!  ") + ".txt"
        print("Vi har fått orden.\nTack för ditt samverkan")
        myfile = open(filename, "w")
        myfile.write(nyord)
        myfile.close()
        Meny = False
        
    elif option == "4":
        print("Programmet avslutas Välkommen åter")
        Meny = False


    
    

        


