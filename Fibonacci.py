import datetime

def fibonacci_recursivo(limite, a=0, b=1):
    if a >= limite:
        return []
    else:
        return [a] + fibonacci_recursivo(limite, b, a + b)

def fibonacci_iterativo(limite):
    a, b = 0, 1
    lista = []
    while a < limite:
        lista.append(a)
        a, b = b, a + b
    return lista

limite = int(input('Insira um número: '))

start_time = datetime.datetime.now()
print("\n\nLista ordenada pelo método iterativo do Fibonacci: \n", fibonacci_iterativo(limite))
end_time = datetime.datetime.now()
tempoIterativo = (end_time-start_time)
print(f"Tempo levado para resolução pelo método iterativo: {tempoIterativo} segundos.")

start_time = datetime.datetime.now()
print("\n\nLista ordenada pelo método recursivo do Fibonacci: \n", fibonacci_recursivo(limite))
end_time = datetime.datetime.now()
tempoRecursivo = (end_time-start_time)
print(f"Tempo levado para resolução pelo método recursivo: {tempoRecursivo} segundos.")

diferençaTempo = abs(tempoIterativo - tempoRecursivo)
if tempoIterativo < tempoRecursivo:
    print("\nO método iterativo foi mais rápido do que o método recursivo.")
    print("Diferença de tempo:", diferençaTempo)
elif tempoIterativo > tempoRecursivo:
    print("\nO método recursivo foi mais rápido do que o método iterativo.")
    print("Diferença de tempo:", diferençaTempo)
else:
    print("\nO método iterativo e o método recursivo tiveram o mesmo tempo de execução.")
    print("Tempo levado:", tempoIterativo)