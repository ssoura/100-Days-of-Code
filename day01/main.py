# Band Name Generator

print("Welcome to the Band Name Generator.")

# initialize the variables 
city = ""
pet_name = ""

# check user has entered something
while True:
    print("What's the name of the city you grew up in?")
    city = input("> ")
    # if there's no input, ask again
    if city == "":
        print("You haven't entered anything. Please try again.")
    else:
        break

while True:
    print("What's your pet's name?")
    pet_name = input("> ")
    if pet_name == "":
        print("You haven't entered anything. Please try again.")
    else:
        break

# output using f-strings
print(f"Your band name : {city} {pet_name}.")
