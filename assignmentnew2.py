# Assignment-3: Searching & Sorting
    # Implement Binary Search
    # Implement Merge Sort
    # Implement Quick Sort
    # Implement Insertion Sort
    # Write a program to sort list of strings (similar to that of dictionary)

# 1. solution -- Implement Binary Search

def binary_search(arr, target):
    low, high = 0, len(arr) - 1

    while low <= high:
        mid = (low + high) // 2
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            low = mid + 1
        else:
            high = mid - 1

    return -1

# 2. Solution -- Implemment Merge Sort


def merge_sort(arr):
    if len(arr) <= 1:
        return arr

    mid = len(arr) // 2
    left_half = merge_sort(arr[:mid])
    right_half = merge_sort(arr[mid:])

    return merge(left_half, right_half)


def merge(left, right):
    merged = []
    left_index, right_index = 0, 0

    while left_index < len(left) and right_index < len(right):
        if left[left_index] < right[right_index]:
            merged.append(left[left_index])
            left_index += 1
        else:
            merged.append(right[right_index])
            right_index += 1

    merged.extend(left[left_index:])
    merged.extend(right[right_index:])

    return merged


# 3. Implement Quick Sort:

def quick_sort(arr):
    if len(arr) <= 1:
        return arr

    pivot = arr[len(arr) // 2]
    left = [x for x in arr if x < pivot]
    middle = [x for x in arr if x == pivot]
    right = [x for x in arr if x > pivot]

    return quick_sort(left) + middle + quick_sort(right)

# 4. Implement insertion sort: 
def insertion_sort(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        while j >= 0 and arr[j] > key:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key



# 5. Write a program to sort list of strings (similar to that of dictionary)

def dictionary_sort(strings_list):
    return sorted(strings_list, key=lambda s: s.lower())


strings_list = ["Aeroplane", "Cat", "Bat", "Zebra"]
sorted_list = dictionary_sort(strings_list)
print(sorted_list)  # Output: ['Aeroplane', 'Bat', 'Cat', 'Zebra']
