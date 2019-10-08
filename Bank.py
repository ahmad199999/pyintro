
user = "AhmadMirzad" # En sträng variabel som innehåller en användernamn
userName = (input("write in your username:")) # Input är en funktion som frågar användaren om att skriva in sitt användernamn
if user != userName:  # If (om) är en vilkor satts och det här är != inte lika med tecken. Här frågas om user är inte lika med username stäng av programmet.
    exit() # gå ut eller stäng av.

hometown = "Kabul" # En variabel som innehåller en datatyp av sträng. Den variabeln ska vara en säkerhet fråga till användaren.
town = input("where is your hometown?:") # Input en funktion som frågar användare att skriva in sitt hemstad.
if town != hometown: # En vilkor satts som säkerställer om användaren skriver fel hemstaden logas den ut med hjälp exit().
    exit()

age = 21
userage = int(input("how old are you?:"))
if userage != age:
    exit()

bank = "Swedbank"
userbank = input("Which bank do you want to contact?:")
if userbank != bank:
    exit()


pin = 1234 # En integer eller heltal variabel som innehåller lösenord till användaren som vill loga in i programmet.
userPin = int(input("write in your password:")) # int och input eller en heltal och en funktion som båda vill underlätta fär användaren
if pin != userPin:                                                                              # skriva in lösenordet med heltal
    exit()    
print("Dear Ahmad Mirzad wellcome to your bank!")

try:
    with open("balance.txt", "r")as balanceFile:
        try:
            balance = balanceFile.readline()
            balance = float(balance)
        except (ValueError):
            print("File corrupt")
            balance = 0.0
except (FileNotFoundError):
    balance = 0.0
menu = 0

while menu != 3:
    print("Ditt saldo är:", balance)
    menu = int(input("skriv ditt val:[1,2,3] "))
    if menu == 1:
        balance = balance + float(input("hur mycket vill du sätta in:"))

    elif menu == 2:
        print("Utagg")
        balance = balance - int(input("hur mycket vill du ta ut:"))
        
    else:
        print("Fel eller avslut") 
        print("Fel eller avslut")
        try:
            with open("balance.txt", "w")as balanceFile:
                balanceFile.write(str(balance))
        except (FileNotFoundError):
            print("Ingen fil") 


        

