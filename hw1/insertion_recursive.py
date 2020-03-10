import time
import random
import sys


def insertion_recursive(arr, n):
    if n > 1:
        insertion_recursive(arr, n - 1)
        j = n - 2
        key = arr[n - 1]
        while arr[j] >= key and j >= 0:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key


# print(sys.getrecursionlimit())
# sys.setrecursionlimit(10010)
# print(sys.getrecursionlimit())
arr_range = 100
test_arr = [random.randint(1, 10000) for x in range(arr_range)]
print("The starting array is: {}".format(test_arr))
start = time.time()
insertion_recursive(test_arr, len(test_arr))
end = time.time()
print("Time needed to sort using recursive insertion: {:f}".format(end - start))
print("The sorted array is: {}".format(test_arr))
