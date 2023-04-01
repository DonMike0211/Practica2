def merge_sort(arr):
    # Verificar si la lista está vacía o tiene un solo elemento
    if len(arr) <= 1:
        return arr
    else:
        # Dividir la lista en dos mitades
        mid = len(arr) // 2
        left = arr[:mid]
        right = arr[mid:]
        
        # Aplicar recursivamente MergeSort a las dos mitades
        left_sorted = merge_sort(left)
        right_sorted = merge_sort(right)
        
        # Mezclar las dos mitades ordenadas
        merged = []
        i = j = 0
        while i < len(left_sorted) and j < len(right_sorted):
            if left_sorted[i] < right_sorted[j]:
                merged.append(left_sorted[i])
                i += 1
            else:
                merged.append(right_sorted[j])
                j += 1
        merged += left_sorted[i:]
        merged += right_sorted[j:]
        return merged

# Ejemplo de uso
arr = [64, 34, 25, 12, 22, 11, 90]
sorted_arr = merge_sort(arr)
print("Arreglo ordenado:")
print(sorted_arr)

