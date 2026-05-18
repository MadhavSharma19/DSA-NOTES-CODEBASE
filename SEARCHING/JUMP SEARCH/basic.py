import math

def jump_search(arr, target):
    n = len(arr)
    step = int(math.sqrt(n))  # block size

    prev = 0

    # Jumping phase
    while prev < n and arr[min(step, n) - 1] < target:
        prev = step
        step += int(math.sqrt(n))
        if prev >= n:
            return -1

    # Linear search phase
    while prev < min(step, n):
        if arr[prev] == target:
            return prev
        prev += 1

    return -1


# Example
arr = [1, 3, 5, 7, 9, 11, 13, 15]
target = 9

result = jump_search(arr, target)

if result != -1:
    print("Element found at index:", result)
else:
    print("Element not found")