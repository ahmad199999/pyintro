# en slumpgenerator
# program som rullar en tärning

import random # laddar in random klassen så vi kan använda

print("vill du rulla en tärning?") # Meddelande till användaren,försök läsa in sides som en 
# int, vid fel sätt sides till 1
try: # try och except hanterar felet.
    sides = int(input("hur många sidor: "))

except:
    print("tärning behöver 1+ sidor")
    sides = 1
run = "y" # vi ger run värdet y som standard
while run.lower()== "y":
    randomNumber = random.randint(1,sides) # slumpa ett tal mellan 1 och sides




    print(randomNumber) # skrivar ut

    run = input("vill du rulla en till tärning Y/N:")