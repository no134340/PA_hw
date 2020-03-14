import time
import random


def find_sum(arr, s):
    arr.sort()
    print("The sorted array is: {}".format(arr))
    i = 0
    j = len(arr) - 1
    while i < j:
        if arr[i] + arr[j] < s:
            i += 1
        elif arr[i] + arr[j] > s:
            j -= 1
        else:
            return [arr[i], arr[j]]
            break
        print("Subarray: {}".format(arr[i:j + 1]))
    return []


# size of the array
arr_range = 20

# range of the values in the array
values_range = 30

# the sum of the array elements we're searching for
value = 10

test_arr = [random.randint(1, values_range) for x in range(arr_range)]
print("The starting array is: {}".format(test_arr))

start = time.clock()
elems = find_sum(test_arr, value)
end = time.clock()

print("Time needed to do the search: {:f}".format(end - start))
print("The elements of the array are: {}".format(elems))
