import time

def linear_search(arr, target):
    for i in range(len(arr)):
        if arr[i] == target:
            return i
    return -1


arr = [10, 25, 30, 45, 50, 60, 75, 80, 95]
print("original array:",arr)
target = int(input("Enter the element to search: "))

print("\nArray:", arr)

start = time.time()
result = linear_search(arr, target)
end = time.time()

if result != -1:
    print(f"Element {target} found at index {result}")
else:
    print(f"Element {target} not found in the array")

print(f"Execution Time: {end - start:.6f} sec")

print("\nTime Complexity of Linear Search:")
print("Best Case   -> O(1)")
print("Average Case-> O(n)")
print("Worst Case  -> O(n)")


# Binary Search (works only on sorted array)

arr = [10, 20, 30, 40, 50, 60, 70, 80, 90]
print("original array:",arr)
target = int(input("Enter element to search: "))

low = 0
high = len(arr) - 1
found = False

while low <= high:
    mid = (low + high) // 2
    if arr[mid] == target:
        print("Element found at index", mid)
        found = True
        break
    elif arr[mid] < target:
        low = mid + 1
    else:
        high = mid - 1

if not found:
    print("Element not found in the array")

