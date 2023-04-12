from random import choice


# Use a more descriptive variable name than 'list'
my_list = []

while True:
    value = input("Enter a value to add to the list (or 'end' to finish): ")
    if value == 'end':
        break
    try:
        # Check if value is already in the list
        if value in my_list:
            print("This element is already in the list.")
        else:
            # Append the entered value to the list
            my_list.append(value)
    except ValueError:
        print("Invalid value. Please enter a valid value.")

print("The final list is:", my_list)
if len(my_list) >= 2:
    # Choose a random element from the list using the choice() function
    print("The randomly selected element is:", choice(my_list))
else:
    print("The list has less than two elements.")
