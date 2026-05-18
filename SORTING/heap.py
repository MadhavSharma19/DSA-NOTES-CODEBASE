# ---------------- HEAPIFY FUNCTION ----------------
def heapify(arr, n, i):

    largest = i          # Assume root is largest
    left = 2 * i + 1     # Left child
    right = 2 * i + 2    # Right child

    # Check left child
    if left < n and arr[left] > arr[largest]:
        largest = left

    # Check right child
    if right < n and arr[right] > arr[largest]:
        largest = right

    # Swap if needed
    if largest != i:
        arr[i], arr[largest] = arr[largest], arr[i]

        # Heapify affected subtree
        heapify(arr, n, largest)


# ---------------- HEAP SORT FUNCTION ----------------
def heap_sort(arr):

    n = len(arr)

    # Build max heap
    for i in range(n // 2 - 1, -1, -1):
        heapify(arr, n, i)

    # Extract elements one by one
    for i in range(n - 1, 0, -1):

        # Move root to end
        arr[i], arr[0] = arr[0], arr[i]

        # Heapify reduced heap
        heapify(arr, i, 0)


# ---------------- DRIVER CODE ----------------
arr = [12, 11, 13, 5, 6, 7]

print("Original Array:")
print(arr)

heap_sort(arr)

print("Sorted Array:")
print(arr)