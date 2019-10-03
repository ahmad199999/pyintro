
user = "AhmadMirzad"
userName = (input("write in your username:"))
if user != userName:
    exit()

hometown = "Kabul"
town = input("where is your hometown?:")
if town != hometown:
    exit()

age = 21
userage = int(input("how old are you?:"))
if userage != age:
    exit()

bank = "Swedbank"
userbank = input("Which bank do you want to contact?:")
if userbank != bank:
    exit()


pin = 1234
userPin = int(input("write in your password:"))
if pin != userPin:
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


        

