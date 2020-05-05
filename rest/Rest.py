
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
        from difflib import get_close_matches # difflib kan används som ett komparator den jämför filer. Från difflib laddar vi get_close_mutches för att kunna göra våran 
        #Lexikon lite smartare. som till ex om nån skiver waterr med två rr då ger lexikon ett förslag som är korrekt som water eller om det finns nån annan ord som är nära 
        #water ger den förslag. 
        print("Welcome to longman dictionary!") #Om användaren väljar 1 då skrivs denna mening först. 
        mydata = json.load(open("data.json")) #Här skapar vi ett variable och inne i variable öppnar våran json fil som vi har. Vi öppnar den i json.load för att kunna 
        #roppa efter den del av data som vi vill.
        
        def translate(vocabulary): #Här skapar vi ett funktion 
            vocabulary = vocabulary.lower() #Variable som är lika med små bokstav som vi representerar ett ord i våra data.
            if vocabulary in mydata: # här har vi en variable och våran data som innehåller Englska ord.
                return mydata[vocabulary] # Om den ord som vi söker finns i database printa den. 
            elif len(get_close_matches(vocabulary, mydata.keys())) > 0: # funktion för att hämta liknande ord från ordboken 
                yn = input("Did you mean %s instead? Enter Y if yes, or N if no: " % get_close_matches(vocabulary, mydata.keys())[0]) # när funktion ger förslag och n betyder nej och y yes.
                if yn == "Y": #Om yes den går ett rad ner och läser.
                    return mydata[get_close_matches(vocabulary, mydata.keys())[0]] 
                elif yn == "N": #Om no eller nej den printer nedan raden.
                    return "the vocabulary may not exit in dictionary or dubble check the word."
                else:
                    return " We did not understand your word" #Om användaren väljer annant än da två val, skiver nedre raden.
            else:
                 return "the vocabulary may not exit in dictionary or dubble check the word."
        vocabulary = input("Enter an English word:  ") # Här fråga användaren att skriv ett ord på englska. 
        print(translate(vocabulary)) # Om användaren skriver ett ord som finns i mydata eller database då printas svaret
        Meny = False # Programmet stängs ner.

    elif option == "2": #om option är lika med 2 då läser nedre raden. laddas våran data up.
        import json 
        mydata = json.load(open("data.json"))  #laddas våran data up. vi har en variable som bär våran data i sig.
        print(mydata) #vi säger åt programmet att läsa våran data. 

        Meny = False # Programmet stängs ner.
                   
    elif option == "3": #om option är lika med 3 då läser nedre raden.
        #import os
        nyord = input("Skriv ditt nya ord!  ") #ett variable som bär våran input. vi tar en inputfrån användaren.
        print("Ditt nya ord sparas i en fil! ") #
        filename = input("Vad ska hetta filen!  ") + ".txt" #vi tar en input från avändaren med index txt.
        print("Vi har fått orden.\nTack för ditt samverkan") 
        myfile = open(filename, "w") #Skapas ett fil
        myfile.write(nyord) #nya orden från användaren skrivs.
        myfile.close() #och sen stängs
        Meny = False # Programmet stängs ner.
        
    elif option == "4":  #om option är lika med 4 då läser nedre raden.
        print("Programmet avslutas Välkommen åter")
        Meny = False # Programmet stängs ner.


    
    

        


