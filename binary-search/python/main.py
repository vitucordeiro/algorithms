def binary_search(arr, target):
    low = 0
    high = len(arr) - 1

    while low <= high:
        mid = (low + high) // 2
        mid_val = arr[mid]

        if mid_val == target:
            return mid
        elif mid_val < target:
            low = mid + 1
        else:
            high = mid - 1

    return -1  # Se o elemento não for encontrado

# Exemplo de uso:
arr = [2, 4, 6, 8, 10, 12, 14, 16]
target = 10
result = binary_search(arr, target)
if result != -1:
    print(f'O elemento {target} está na posição {result}.')
else:
    print(f'O elemento {target} não está presente no array.')
