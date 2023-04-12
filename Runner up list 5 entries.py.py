list = []

for i in range(5):
    while True:
        value = input(f"Enter value {i+1} to add to the list: ")
        try:
            num = int(value)
            if num in list:
                print("This number is already in the list.")
            else:
                list.append(num)
                break
        except ValueError:
            print("Invalid value. Please enter an integer.")

list.sort()
print("The final list is:", list)
if len(list) >= 2:
    print("The second largest number is:", list[-2])
else:
    print("The list has less than two elements.")
