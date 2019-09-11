# en slumpgenerator
# program som rullar en tärning

import random

print("vill du rulla en tärning?")
try:
    sides = int(input("hur många sidor: "))

except:
    print("tärning behöver 1+ sidor")
    sides = 1
run = "y"
while run.lower()== "y":
    randomNumber = random.randint(1,sides)



    print(randomNumber)

    run = input("vill du rulla en till tärning Y/N:")