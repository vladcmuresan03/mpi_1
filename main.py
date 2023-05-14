import time
import random


def radix_sort(arr):
    max_value = max(arr)
    num_digits = len(str(abs(max_value)))

    for digit in range(num_digits):
        counting_sort(arr, digit)


def quicksort(arr):
    stack = [(0, len(arr) - 1)]
    while stack:
        low, high = stack.pop()
        if low < high:
            pivot_index = partition(arr, low, high)
            if pivot_index - low < high - pivot_index:
                stack.append((low, pivot_index - 1))
                stack.append((pivot_index + 1, high))
            else:
                stack.append((pivot_index + 1, high))
                stack.append((low, pivot_index - 1))


def partition(arr, low, high):
    pivot = arr[high]
    i = low - 1
    for j in range(low, high):
        if arr[j] <= pivot:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]
    arr[i + 1], arr[high] = arr[high], arr[i + 1]
    return i + 1


def counting_sort(arr, digit):
    n = len(arr)
    count = [0] * 10  
    output = [0] * n  
    for i in range(n):
        index = (arr[i] // (10 ** digit)) % 10
        count[index] += 1
    for i in range(1, 10):
        count[i] += count[i - 1]

    for i in range(n - 1, -1, -1):
        index = (arr[i] // (10 ** digit)) % 10
        output[count[index] - 1] = arr[i]
        count[index] -= 1

    for i in range(n):
        arr[i] = output[i]


def bubble_sort(arr):
    n = len(arr)
    for i in range(n - 1):
        for j in range(n - 1 - i):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]


def heap_sort(arr):
    def heapify(arr, n, i):
        largest = i
        left = 2 * i + 1
        right = 2 * i + 2

        if left < n and arr[i] < arr[left]:
            largest = left

        if right < n and arr[largest] < arr[right]:
            largest = right

        if largest != i:
            arr[i], arr[largest] = arr[largest], arr[i]
            heapify(arr, n, largest)

    n = len(arr)

    # max heap
    for i in range(n // 2 - 1, -1, -1):
        heapify(arr, n, i)

    # elements from the heap in descending order
    for i in range(n - 1, 0, -1):
        arr[i], arr[0] = arr[0], arr[i]
        heapify(arr, i, 0)

def bucket_sort(arr):
    n = len(arr)
    min_value = min(arr)
    max_value = max(arr)
    bucket_size = (max_value - min_value) // n + 1
    buckets = []
    for _ in range(n):
        buckets.append([])

    for num in arr:
        index = (num - min_value) // bucket_size
        buckets[index].append(num)

    sorted_arr = []
    for bucket in buckets:
        insertion_sort(bucket)
        sorted_arr.extend(bucket)

    for i in range(n):
        arr[i] = sorted_arr[i]

def insertion_sort(arr):
    n = len(arr)
    for i in range(1, n):
        key = arr[i]
        j = i - 1
        while j >= 0 and arr[j] > key:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key

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

def generate_random_numbers(n, start_range, end_range):
    numbers = []
    for _ in range(n):
        number = random.randint(start_range, end_range)
        numbers.append(number)
    return numbers

def main():
    n = 30000  # number of numbers
    start_range = 0  # start range (inclusive)
    end_range = 100000000  # end range (inclusive)

    array = generate_random_numbers(n, start_range, end_range)

    print("Sorting Algorithms:")
    print("1. Quicksort")
    print("2. Radix Sort")
    print("3. Bubble Sort")
    print("4. Heap Sort")
    print("5. Bucket Sort")
    print("6. Merge Sort")

    choice = int(input("Enter your choice (1-6): "))

    if choice == 1:
        sorting_algorithm = quicksort
    elif choice == 2:
        sorting_algorithm = radix_sort
    elif choice == 3:
        sorting_algorithm = bubble_sort
    elif choice == 4:
        sorting_algorithm = heap_sort
    elif choice == 5:
        sorting_algorithm = bucket_sort
    elif choice == 6:
        sorting_algorithm = merge_sort
    else:
        print("Invalid choice.")
        return

    start_time = time.time()
    sorting_algorithm(array)
    end_time = time.time()

    sorting_time = end_time - start_time
    print(f"Sorted array: {array[:10]} ... {array[-10:]}")
    print(f"Sorting time: {sorting_time} seconds")

if __name__ == '__main__':
    main()
