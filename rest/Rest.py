




Meny = True
option = 0
print("Hej och Välkommen! ")
print("Du har fyra val!")
while Meny:
    option = input('''
Översättning från engelska till engelska [1] 
Att känna till alla ord i ordboken [2]
[3]spara loggar till fil
[4]Avsluta programmet
Ditt Val:''')

    if option == "1":
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
        f = open("wiki.txt", "r")
        
    elif option == "4":
        print("Programmet avslutas Välkommen åter")
        Meny = False


    
    
        


