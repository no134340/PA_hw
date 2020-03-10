import time
import random
import sys
from merge_module import merge_sort


def find_sum(arr, s):
    arr = merge_sort(arr)
    i = 0
    j = len(arr) - 1
    elems = []
    while i < j:
        if arr[i] + arr[j] < s:
            i += 1
        elif arr[i] + arr[j] > s:
            j -= 1
        else:
            elems.append([arr[i], arr[j]])
            break
    return elems, arr


# print(sys.getrecursionlimit())
# sys.setrecursionlimit(10010)
# print(sys.getrecursionlimit())
arr_range = 100
test_arr = [random.randint(1, 20) for x in range(arr_range)]
print("The starting array is: {}".format(test_arr))
start = time.time()
elems, array = find_sum(test_arr, 10)
end = time.time()
print("The array after the search is: {}".format(array))
print("Time needed to do the search: {:f}".format(end - start))
print("The elements are array is: {}".format(elems))
