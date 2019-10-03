file = open("test.txt", "r+")
test = file.read()
print(test)

test = input("skrive nåt:")
file.write(test)
file.close()