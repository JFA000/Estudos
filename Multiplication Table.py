def multiplicate(x):
    
    for i in range(1,11):
        print(f"{x} * {i} = {x*i}")

num = float(input("Select number to insert in multiplication table: "))
multiplicate(num)