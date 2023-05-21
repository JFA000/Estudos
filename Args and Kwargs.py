#Crie uma função que receba um número variável de argumentos e retorne a soma desses argumentos.
#Crie uma função que receba um número variável de argumentos e retorne o maior valor entre eles.
#Crie uma função que receba um número variável de argumentos e retorne o menor valor entre eles.
#Crie uma função que receba um número variável de argumentos e retorne a média desses argumentos.

def ListSum():
    NSoma = []
    print("\nSelecting numbers to sum")
    while True:
        valor = input("Enter a number or ‘end’ to finish: ")
        if valor == 'end':
            break
        NSoma.append(int(valor))
    return sum(NSoma)

def ListMaximum():
    NSoma = []
    print("\nSelecting numbers to find Maximum")
    while True:
        valor = input("Enter a number or ‘end’ to finish: ")
        if valor == 'end':
            break
        NSoma.append(int(valor))
    return max(NSoma)

def ListMinimum():
    NSoma = []
    print("\nSelecting numbers to find minimum")
    while True:
        valor = input("Enter a number or ‘end’ to finish: ")
        if valor == 'end':
            break
        NSoma.append(int(valor))
    return min(NSoma)

def ListAverage():
    NSoma = []
    print("\nSelecting numbers to average")
    while True:
        valor = input("Enter a number or ‘end’ to finish: ")
        if valor == 'end':
            break
        NSoma.append(int(valor))
    return sum(NSoma)/len(NSoma)

#print("\nList Sum: ", ListSum(), "\nList Maximum: ",ListMaximum(), "\nList Minimum: ", ListMinimum(), "\nList Average: ", ListAverage())

def list_stats():
    lst = []
    while True:
        valor = input("Enter a number or 'end' to finish: ")
        if valor == 'end':
            break
        lst.append(int(valor))
    return sum(lst), max(lst), min(lst), sum(lst)/len(lst)

NumberSum, NumberMax, NumberMin, NumberAvg = list_stats()
print(f"The sum of the numbers is: {NumberSum}")
print(f"The max of the numbers is: {NumberMax}")
print(f"The min of the numbers is: {NumberMin}")
print(f"The avg of the numbers is: {NumberAvg}")