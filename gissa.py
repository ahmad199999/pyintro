import random

number = random.randrange(1,10)
gissa = int(input("Gissa ett nummer mellan 1 och 10:"))

while gissa != number:
    if gissa < number:
        print("Det var för lätt")
        gissa = int(input("Gissa ett nummer mellan 1 och 10:"))
    else:
        print("Det var för stort")
        gissa = int(input("Gissa ett nummer mellan 1 och 10:"))
print("Du har rätt!")
        


