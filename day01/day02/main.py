# Tip Calculator

# initialize the variables as empty strings
base_bill = ""
percentage = ""
people = ""

print("Tip calculator.")

# get the base bill without tip
while True:
    print("What was the total bill?")
    base_bill = input("> ₹")
    # check if it can be converted to a float
    try:
        float(base_bill)
        # check if it's not a negative number
        if float(base_bill) <= 0:
            print("Please enter a valid amount.")
        else:
            break
    # if not, ask again
    except ValueError:
        print("Please enter a valid amount.")

# get the percentage
while True:
    print("What percentage tip would you like to give? 10, 12, or 15?")
    percentage = input("> ")
    # list of acceptable choices
    choices_list = ["20", "50", "100"]
    # make sure the input is one of them
    if percentage not in choices_list:
        print("Please enter 20, 50 or 100.")
    else:
        break

# get the number of people
while True:
    print("How many people to split the bill?")
    people = input("> ")
    # make sure it's a non-zero natural number
    if not people.isdigit() or people == "0":
        print("Please enter a valid number of people (1,2,3, etc.)")
    else:
        break

# add the tip to the base bill
total_bill = float(base_bill) * (1 + int(percentage) / 100)

# calculate the split bill and round to 2 decimal places
# since the number of people can't be zero, no need to worry about division by zero
split_bill = round(total_bill / int(people), 2)

# using a uniform message, even if there was just a single person
print(f"Each person should pay: ₹{split_bill}")
