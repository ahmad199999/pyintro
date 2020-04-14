
Meny = True
option = 0
print("Hej och Välkommen! ")
print("Du har fyra val!")
while Meny:
    option = input('''
Lexikon Engelska till Engelska [1] 
Vill du kolla upp alla ord i lexikon med dessa betydelse [2]
Saknas ord i lexikon skriv till oss [3]
Vill du avsluta programmet [4]
Ditt Val:''')
    if option > "4":
        print("Du måste välja ett tal mellan 1 och 4!\n ")

    elif option == "1":
        import json
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


    
    

        


