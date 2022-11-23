array = ["Star Wars", "Leon Killer", "Eternals", "Uncharted"]
st= str(array)
file = open("films.txt", "w")
file.write(st)
file.close()
file = open("films.txt", "r")
print(file.read())
