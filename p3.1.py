import time
import random
import matplotlib.pyplot as plt

# Bubble Sort
def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        for j in range(0, n-i-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
    return arr

# Merge Sort
def merge_sort(arr):
    if len(arr) > 1:
        mid = len(arr) // 2
        left = arr[:mid]
        right = arr[mid:]

        merge_sort(left)
        merge_sort(right)

        i = j = k = 0
        while i < len(left) and j < len(right):
            if left[i] < right[j]:
                arr[k] = left[i]
                i += 1
            else:
                arr[k] = right[j]
                j += 1
            k += 1

        while i < len(left):
            arr[k] = left[i]
            i += 1
            k += 1

        while j < len(right):
            arr[k] = right[j]
            j += 1
            k += 1
    return arr

# Quick Sort
def quick_sort(arr):
    if len(arr) <= 1:
        return arr
    else:
        pivot = arr[0]
        left = [x for x in arr[1:] if x < pivot]
        right = [x for x in arr[1:] if x >= pivot]
        return quick_sort(left) + [pivot] + quick_sort(right)

# Time Comparison
def compare_sorting_algorithms(n_values):
    bubble_times = []
    merge_times = []
    quick_times = []

    for n in n_values:
        arr = random.sample(range(n * 10), n)

        # Bubble Sort
        start_time = time.time()
        bubble_sort(arr.copy())
        bubble_times.append(time.time() - start_time)

        # Merge Sort
        start_time = time.time()
        merge_sort(arr.copy()) 
        merge_times.append(time.time() - start_time)

        # Quick Sort
        start_time = time.time()
        quick_sort(arr.copy())
        quick_times.append(time.time() - start_time)

    return bubble_times, merge_times, quick_times


def plot_comparison(n_values, bubble_times, merge_times, quick_times):
    plt.plot(n_values, bubble_times, label="Bubble Sort")
    plt.plot(n_values, merge_times, label="Merge Sort")
    plt.plot(n_values, quick_times, label="Quick Sort")
    plt.xlabel('Number of Elements')
    plt.ylabel('Time (seconds)')
    plt.legend()
    plt.show()


n_values = [100, 574, 1368, 2192, 5424, 10430]
bubble_times, merge_times, quick_times = compare_sorting_algorithms(n_values)
plot_comparison(n_values, bubble_times, merge_times, quick_times)
