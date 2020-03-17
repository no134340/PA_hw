import custom_heap as hp


def merge_lists(arrays, n):
    pass
    merged = []
    heap_arr = []
    indices = [0 for x in range(n)]
    main_heap = hp.MinHeap()
    for arr in arrays:
        heap_arr.append(arr[0])
    main_heap.build_heap(heap_arr)

    while sum(indices) != k * n:
        elem = main_heap.extract_top()
        merged.append(elem[0])
        indices[elem[1]] += 1
        if indices[elem[1]] < n:
            main_heap.heap_insert(arrays[elem[1]][indices[elem[1]]])
    return merged


if __name__ == '__main__':
    import random
    import time

    k = 4
    n = 16
    rand_range = 100
    arrays = []
    for i in range(k):
        tmp = [random.randint(1, rand_range) for j in range(n)]
        tmp.sort()
        print(tmp)
        paired = [[t, i] for t in tmp]
        arrays.append(paired)
    merged = merge_lists(arrays, n)
    print(merged)
