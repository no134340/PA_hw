"""
ZADATAK 3
INPUT:
    k sorted arrays in increasing order totaling in n elements.
OUTPUT:
    One sorted array consisting of n elements of k initial arrays.
    (merged k initial arrays).
IDEA:
    Use min heap to merge the arrays.
"""

import custom_min_heap as hp


def merge_lists(arrays, n):
    # the output array
    merged = []

    # the temp array we will build heap from initially
    heap_arr = []

    # we will store the indices of top element from each array
    # just so we know which element to take next and when to stop
    indices = [0 for x in range(k)]

    # make a new min heap
    # we're storing the elements from the array as
    # a two element list [elem, ind]
    # where elem is the original value
    # and ind is the index of the list it came from (0, 1, ..., k - 1)
    main_heap = hp.MinHeap()
    for i in range(len(arrays)):
        heap_arr.append([arrays[i][0], i])
    main_heap.build_heap(heap_arr)

    # the loop will stop when we've reached ends of all k lists
    while sum(indices) != n:
        # take the min element from the heap and place it into the main array
        elem = main_heap.extract_top()
        merged.append(elem[0])

        # increase the index at the array the extracted min element came from
        indices[elem[1]] += 1

        # if it didn't reach the end of that array, place the next element
        # into the min heap
        if indices[elem[1]] < len(arrays[elem[1]]):
            main_heap.heap_insert([arrays[elem[1]][indices[elem[1]]], elem[1]])

    return merged


if __name__ == '__main__':
    import random
    import time

    # number of arrays
    k = 4

    # number of elements each array will have
    nk = [random.randint(1, 32) for i in range(k)]

    rand_range = 100
    arrays = []
    for i in range(k):
        tmp = [random.randint(1, rand_range) for j in range(nk[i])]
        tmp.sort()
        print(tmp)
        arrays.append(tmp)

    print("k = {}, n = {}".format(k, sum(nk)))
    merged = merge_lists(arrays, sum(nk))
    print(merged)
