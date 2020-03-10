import math


def merge(left, right):
    arr = []
    n = len(right) + len(left)
    left.append(math.inf)
    right.append(math.inf)
    lind, rind = 0, 0
    for i in range(n):
        if left[lind] > right[rind]:
            arr.append(right[rind])
            rind += 1
        else:
            arr.append(left[lind])
            lind += 1
    return arr


def merge_sort(arr):
    if len(arr) > 1:
        div = len(arr) // 2
        left_array = merge_sort(arr[:div])
        right_array = merge_sort(arr[div:])
        sorted_arr = merge(left_array, right_array)
        return sorted_arr
    else:
        return arr


if __name__ == '__main__':
    import random
    import sys

    print(sys.getrecursionlimit())
    arr_range = 10
    test_arr = [random.randint(1, 20) for x in range(arr_range)]
    print("The original array is: {}".format(test_arr))
    test_arr = merge_sort(test_arr)
    print("The sorted array is: {}".format(test_arr))
