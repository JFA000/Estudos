import random
import datetime


randomlist = []
for i in range(0, 2000):
    n = random.randint(1, 99)
    randomlist.append(n)

print("Lista de 2000 números aleatórios criada para ser ordenada!\n")

# Bubble Sort
start_time = datetime.datetime.now()
listamodo1 = randomlist.copy()
for i in range(len(listamodo1)):
    for j in range(len(listamodo1) - 1):
        if listamodo1[j] > listamodo1[j + 1]:
            listamodo1[j], listamodo1[j + 1] = listamodo1[j + 1], listamodo1[j]
end_time = datetime.datetime.now()
bubble_sort_time = end_time - start_time
print("Lista ordenada pelo método Bubble Sort:")
print("Header:", listamodo1[:10], "..." if len(listamodo1) > 10 else "")
print("Tempo levado pelo Bubble Sort:", bubble_sort_time)

print("\n")

# Merge Sort
def merge_sort(arr):
    if len(arr) <= 1:
        return arr
    mid = len(arr) // 2
    left = merge_sort(arr[:mid])
    right = merge_sort(arr[mid:])
    return merge(left, right)

def merge(left, right):
    result = []
    i = j = 0
    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1
    while i < len(left):
        result.append(left[i])
        i += 1
    while j < len(right):
        result.append(right[j])
        j += 1
    return result

start_time = datetime.datetime.now()
listamodo2 = merge_sort(randomlist.copy())
end_time = datetime.datetime.now()
merge_sort_time = end_time - start_time
print("Lista ordenada pelo método Merge Sort:")
print("Header:", listamodo2[:10], "..." if len(listamodo2) > 10 else "")
print("Tempo levado pelo Merge Sort:", merge_sort_time)

print("\n")

# Compare time differences
time_difference = abs(bubble_sort_time - merge_sort_time)
if bubble_sort_time < merge_sort_time:
    print("Bubble Sort foi mais rápido do que Merge Sort.")
    print("Diferença de tempo:", time_difference)
elif bubble_sort_time > merge_sort_time:
    print("Merge Sort foi mais rápido do que Bubble Sort.")
    print("Diferença de tempo:", time_difference)
else:
    print("Bubble Sort e Merge Sort tiveram o mesmo tempo de execução.")
    print("Tempo levado:", bubble_sort_time)

