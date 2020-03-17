"""
Max heap and min heap implemented using heap types inside one class
"""

from math import ceil
from math import log2
from math import inf


def left(i):
    return 2 * i + 1


def right(i):
    return 2 * i + 2


def parent(i):
    return (i - 1) // 2


class Heap:

    def __init__(self, heap_type='max'):
        self.heap_type = heap_type
        self.heap = []
        self.sorted = []
        self.height = 0
        self.length = len(self.heap)

    def __len__(self):
        return len(self.heap)

    def __str__(self):
        ret_val = ""
        tab_num = self.height
        k = 0
        for i in range(self.height):
            j = i + 1
            ret_val += "   " * tab_num * 2
            while k <= (2 ** j - 2) and k < len(self.heap):
                ret_val += "({})".format(self.heap[k]) + "   " * tab_num
                k += 1
            ret_val += "\n"
            tab_num -= 1
        return ret_val

    def get_height(self):
        return ceil(log2(self.length + 1))

    def heapify(self, i):
        if self.heap_type == 'max':
            l = left(i)
            r = right(i)

            largest = i
            if l <= (self.length - 1) and self.heap[l] > self.heap[i]:
                largest = l
            if r <= (self.length - 1) and self.heap[r] > self.heap[largest]:
                largest = r

            if largest != i:
                self.heap[i], self.heap[largest] = self.heap[largest], self.heap[i]
                self.heapify(largest)
        else:
            l = left(i)
            r = right(i)

            smallest = i
            if l <= (self.length - 1) and self.heap[l] < self.heap[i]:
                smallest = l
            if r <= (self.length - 1) and self.heap[r] < self.heap[smallest]:
                smallest = r

            if smallest != i:
                self.heap[i], self.heap[smallest] = self.heap[smallest], self.heap[i]
                self.heapify(smallest)

    def build_heap(self, arr):
        self.heap = list(arr)
        self.length = len(self.heap)
        self.height = self.get_height()
        for i in range(self.length // 2, -1, -1):
            self.heapify(i)

    def sort(self):
        length = self.length
        temp = list(self.heap)
        for i in range(length - 1, -1, -1):
            self.heap[i], self.heap[0] = self.heap[0], self.heap[i]
            self.length -= 1
            self.heapify(0)
        self.sorted = self.heap
        self.heap = temp
        self.length = len(self.heap)
        return self.sorted

    def extract_top(self):
        top = self.heap[0]
        self.heap[0] = self.heap[self.length - 1]
        self.heap.pop(self.length - 1)
        self.length -= 1
        self.heapify(0)
        return top

    def increase_key(self, i, key):
        if self.heap_type == 'max' and key > self.heap[i]:
            self.heap[i] = key
            while i > 0 and self.heap[i] > self.heap[parent(i)]:
                self.heap[i], self.heap[parent(i)] = self.heap[parent(i)], self.heap[i]
                i = parent(i)
            return i

    def decrease_key(self, i, key):
        if self.heap_type == 'min' and key < self.heap[i]:
            self.heap[i] = key
            while i > 0 and self.heap[i] < self.heap[parent(i)]:
                self.heap[i], self.heap[parent(i)] = self.heap[parent(i)], self.heap[i]
                i = parent(i)
            return i

    def heap_insert(self, key):
        self.length += 1
        if self.heap_type == 'max':
            self.heap.append(-inf)
            ind = self.increase_key(self.length - 1, key)
        else:
            self.heap.append(inf)
            ind = self.decrease_key(self.length - 1, key)
        return ind

    def heap_delete(self, i):
        deleted = self.heap[i]
        if self.heap_type == 'max':
            self.increase_key(i, inf)
        else:
            self.decrease_key(i, -inf)
        self.extract_top()
        return deleted


if __name__ == '__main__':
    import random

    rand_range = 30
    arr_size = 9
    arr = [random.randint(1, rand_range) for i in range(arr_size)]
    print("Original array: {}".format(arr))

    # initialize and make max heap object from array
    max_heap = Heap('max')
    max_heap.build_heap(arr)
    # print built max heap
    print("Max heap:")
    print(max_heap)

    # sort the heap
    sorted_arr = max_heap.sort()
    print("Sorted increasing order using max heap:")
    print(sorted_arr)

    # delete an element from heap and print new heap
    di = 6
    deleted = max_heap.heap_delete(di)
    print("Deleted element {} from heap: {}".format(di, deleted))
    print("Heap after deletion:")
    print(max_heap)

    # insert an element into the heap and print new heap
    inserted = 18
    ind = max_heap.heap_insert(inserted)
    print("Inserted element at index {} to heap: {}".format(ind, inserted))
    print("Heap after insertion:")
    print(max_heap)

    # initialize and make min heap object from array
    min_heap = Heap('min')
    min_heap.build_heap(arr)
    # print built min heap
    print("Min heap:")
    print(min_heap)

    # sort the heap
    sorted_min = min_heap.sort()
    print("Sorted decreasing order using min heap:")
    print(sorted_min)

    # delete an element from heap and print new heap
    di_min = 6
    deleted_min = min_heap.heap_delete(di)
    print("Deleted element {} from heap: {}".format(di_min, deleted_min))
    print("Heap after deletion:")
    print(min_heap)

    # insert an element into the heap and print new heap
    inserted_min = 5
    ind_min = min_heap.heap_insert(inserted_min)
    print("Inserted element at index {} to heap: {}".format(ind_min, inserted_min))
    print("Heap after insertion:")
    print(min_heap)
