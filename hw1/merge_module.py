import math


def merge(arr, p, q, r):
    left = list(arr[p:r + 1])
    left.append(math.inf)
    right = list(arr[r + 1:q + 1])
    right.append(math.inf)
    lind, rind = 0, 0
    for i in range(p, q + 1):
        if left[lind] > right[rind]:
            arr[i] = right[rind]
            rind += 1
        else:
            arr[i] = left[lind]
            lind += 1


def merge_sort(arr, p, q):
    if p < q:
        div = (q + p) // 2
        merge_sort(arr, p, div)
        merge_sort(arr, div + 1, q)
        merge(arr, p, q, div)


if __name__ == '__main__':
    import random
    import sys

    print(sys.getrecursionlimit())
    arr_range = 200
    test_arr = [random.randint(1, 20) for x in range(arr_range)]
    print("The original array is: {}".format(test_arr))
    merge_sort(test_arr, 0, len(test_arr) - 1)
    print("The sorted array is: {}".format(test_arr))
