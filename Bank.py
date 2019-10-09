
user = "AhmadMirzad" # En sträng variabel som innehåller en användernamn
userName = (input("write in your username:")) # Input är en funktion som frågar användaren om att skriva in sitt användernamn
if user != userName:  # If (om) är en vilkor satts och det här är != inte lika med tecken. Här frågas om user är inte lika med username stäng av programmet.
    exit() # gå ut eller stäng av.

hometown = "Kabul" # En variabel som innehåller en datatyp av sträng. Den variabeln ska vara en säkerhet fråga till användaren.
town = input("where is your hometown?:") # Input en funktion som frågar användare att skriva in sitt hemstad.
if town != hometown: # En vilkor satts som säkerställer om användaren skriver fel hemstaden logas den ut med hjälp exit().
    exit()

age = 21 # En variabel som innehåller ålder till användaren
userage = int(input("how old are you?:")) # Input och int som frågar användare att skriva sin ålder med heltal.
if userage != age: # Vilkorsatts som jämför användarens ålder.
    exit()

bank = "Swedbank" # En sträng variabel
userbank = input("Which bank do you want to contact?:") # Variabel och funktion som vill fråga vilken bank vill användare ansluta sig till.
if userbank != bank:
    exit()


pin = 1234 # En integer eller heltal variabel som innehåller lösenord till användaren som vill loga in i programmet.
userPin = int(input("write in your password:")) # int och input eller en heltal och en funktion som båda vill underlätta fär användaren
if pin != userPin:                                      # skriva in lösenordet med heltal
 # en vilkorsatts som lösenordet som finns inne i datoren minne   
  # med den som användaren skriver in och om båda lösenord är samma går användaren till nästa steg annurs logar ut användaren.  
    exit()    
print("Dear Ahmad Mirzad wellcome to your bank!") # Skriver ut ett meddelande till användaren.

try:
    with open("balance.txt", "r")as balanceFile: # vill läsa en fil som heter banlance.txt med hjälp av ("r")
        try:
            balance = balanceFile.readline()  # Försöker läsa filen
            balance = float(balance) # Balance ska läsas i decimal
        except (ValueError): # try och except är för felhantering. 
            print("File corrupt") # om det händer nåt fel då skrivas ut File corrupt istället för andra varningar.
            balance = 0.0 # om det inte finns en fil med namnen balance.txt då sättas balance till 0.0
except (FileNotFoundError):
    print("FIlen fanns inte") 
    balance = 0.0
menu = 0 # Ett variabel

while menu != 3: # while loopen kör runt tills man når 3
    print("Ditt saldo är:", balance) # visra hur mycket vi har i kontot. 
    menu = int(input("skriv ditt val:[1,2,3] ")) # 
    if menu == 1: 
        balance = balance + float(input("hur mycket vill du sätta in:"))

    elif menu == 2:
        print("Utagg")
        balance = balance - int(input("hur mycket vill du ta ut:"))
        
    else:
        print("Fel eller avslut") 
        print("Fel eller avslut")
        try:
            with open("balance.txt", "w")as balanceFile: # vill skriva balance.txt om det inte finns då skapar den med hjälp av ("w")
                balanceFile.write(str(balance)) # Skriver balnacen i sträng.
        except (FileNotFoundError):
            print("Ingen fil") 


        

