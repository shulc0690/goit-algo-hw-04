import timeit
import random


# Сортування злиттям
def merge_sort(arr):
    if len(arr) > 1:
        mid = len(arr) // 2
        left_half = arr[:mid]
        right_half = arr[mid:]

        merge_sort(left_half)
        merge_sort(right_half)

        i = j = k = 0

        while i < len(left_half) and j < len(right_half):
            if left_half[i] < right_half[j]:
                arr[k] = left_half[i]
                i += 1
            else:
                arr[k] = right_half[j]
                j += 1
            k += 1

        while i < len(left_half):
            arr[k] = left_half[i]
            i += 1
            k += 1

        while j < len(right_half):
            arr[k] = right_half[j]
            j += 1
            k += 1


# Сортування вставками
def insertion_sort(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        while j >= 0 and key < arr[j]:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key


# Генерація массиву даних
data = [random.randint(0, 100000) for _ in range(10000)]

# Час сортування злиттям
merge_sort_time = timeit.timeit("merge_sort(data.copy())", globals=globals(), number=1)
print(f"Час сортування злиттям: {merge_sort_time:.5f} секунд")

# Час сортування вставками
insertion_sort_time = timeit.timeit(
    "insertion_sort(data.copy())", globals=globals(), number=1
)
print(f"Час сортування вставками: {insertion_sort_time:.5f} секунд")

# Час сортування Timsort (Python's built-in sorted)
timsort_time = timeit.timeit("sorted(data)", globals=globals(), number=1)
print(f"Час сортування Time: {timsort_time:.5f} секунд")
