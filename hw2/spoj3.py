# TODO
"""
Sphere Online Judge problem (SPOJ) #34875
MINSTOCK - Minimum Stocks
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


class MinHeap():

    def __init__(self):
        self.heap = []
        self.height = 0
        self.length = len(self.heap)

    def __len__(self):
        return len(self.heap)

    def get_height(self):
        return ceil(log2(self.length + 1))

    def build_heap(self, arr):
        self.heap = list(arr)
        self.length = len(self.heap)
        self.height = self.get_height()
        for i in range(self.length // 2, -1, -1):
            self.heapify(i)

    def heapify(self, i):
        l = left(i)
        r = right(i)
        smallest = i

        if l <= (self.length - 1) and self.heap[l][0] < self.heap[i][0]:
            smallest = l
        if r <= (self.length - 1) and self.heap[r][0] < self.heap[smallest][0]:
            smallest = r

        if smallest != i:
            self.heap[i], self.heap[smallest] = self.heap[smallest], self.heap[i]
            self.heapify(smallest)

    def decrease_key(self, i, key):
        if key < self.heap[i][0]:
            self.heap[i][0] = key
            while i > 0 and self.heap[i][0] < self.heap[parent(i)][0]:
                self.heap[i], self.heap[parent(i)] = self.heap[parent(i)], self.heap[i]
                i = parent(i)

    def heap_insert(self, elem):
        key = elem[0]
        self.length += 1
        self.heap.append([inf, elem[1]])
        self.decrease_key(self.length - 1, key)
        self.height = self.get_height()

    def heap_delete(self, i):
        deleted = list(self.heap[i])
        self.decrease_key(i, -inf)
        self.extract_top()
        self.height = self.get_height()
        return deleted

    def extract_top(self):
        top = list(self.heap[0])
        self.heap[0] = list(self.heap[self.length - 1])
        self.heap.pop(self.length - 1)
        self.length -= 1
        self.heapify(0)
        return top


heap = MinHeap()
heap.build_heap([])


def linsearch(x):
    for i in range(len(heap)):
        if heap.heap[i][1] == x:
            return i
    return None


def instruction1(val, key):
    elem = [int(key), val]
    heap.heap_insert(elem)


def instruction2(val, new_key):
    ind = linsearch(val)
    heap.heap_delete(ind)
    heap.heap_insert([int(new_key), val])


def instruction3():
    return heap.extract_top()


day_counter = 0

instr_counter = int(input())
input()
for x in range(instr_counter):
    day_counter += 1
    input()
    instruction = input()
    info = instruction.split(' ')
    if info[0] == '1':
        instruction1(info[1], info[2])
    elif info[0] == '2':
        instruction2(info[1], info[2])
    elif info[0] == '3':
        bought = instruction3()
        print(bought[1] + " " + str(day_counter))

