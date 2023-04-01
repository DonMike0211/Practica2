def quick_sort(arr):
    # Verificar si la lista está vacía o tiene un solo elemento
    if len(arr) <= 1:
        return arr
    else:
        # Seleccionar un elemento pivote y crear sub-listas
        pivot = arr[0]
        left = []
        right = []
        for i in range(1, len(arr)):
            if arr[i] < pivot:
                left.append(arr[i])
            else:
                right.append(arr[i])
        # Aplicar recursivamente QuickSort a las sub-listas izquierda y derecha
        return quick_sort(left) + [pivot] + quick_sort(right)

# Ejemplo de uso
arr = [64, 34, 25, 12, 22, 11, 90]
sorted_arr = quick_sort(arr)
print("Arreglo ordenado:")
print(sorted_arr)

