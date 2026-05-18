def jump_search(arr, target):
    n = len(arr)
    step = 3
    prev = 0

    while prev < n and arr[min(prev + step, n) ] < target:
        prev += step

    for i in range(prev, min(prev + step, n)):
        if arr[i] == target:
            return i

    return -1


arr = [10, 20, 30, 40, 50, 60, 70, 80]
target = 50

result = jump_search(arr, target)

if result != -1:
    print("Element found at index:", result)
else:
    print("Element not found")