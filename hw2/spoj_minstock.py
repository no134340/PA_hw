"""
ZADATAK 4
Sphere Online Judge problem (SPOJ) #34875
MINSTOCK - Minimum Stocks

Using min heap.
SPOJ accepted with time 6.45s and 9.1M

Idea:
    Use min heap to store values of stocks with their names.
    When one wants to buy a stock, simply pop the top element.
    Bottleneck: the linear search to find the element that needs to
    have its key changed.

NOTE:
    When copy-pasting the example input from the SPOJ website,
    html format will recognize newlines between instructions.
    THERE ARE NO NEWLINES BETWEEN INSTRUCTIONS.

    E.g:
    7
    1 ABC 32
    1 XDC 54
    3 BUY
    1 XCD 32
    1 ABC 12
    2 XDC 10
    3 BUY

    NOT:
    7

    1 ABC 32

    1 XDC 54

    3 BUY

    1 XCD 32

    1 ABC 12

    2 XDC 10

    3 BUY
"""
from math import floor
from math import log2
from math import inf
# import sys


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
        if (self.length > 1):
            return floor(log2(self.length))
        else:
            return 0

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


# to make sure the stack won't be broken
# and cause runtime error when testing
# the solution with a large (~10^6) number
# of elements
# uncomment when needed
# sys.setrecursionlimit(500000)

day_counter = 0

instr_counter = int(input())
for x in range(instr_counter):
    day_counter += 1
    instruction = str(input()).strip(' \n')
    info = instruction.split(' ')
    if info[0] == '1':
        elem = [int(info[2]), info[1]]
        heap.heap_insert(elem)
    elif info[0] == '2':
        ind = linsearch(info[1])
        if int(info[2]) > heap.heap[ind][0]:
            heap.heap[ind][0] = int(info[2])
            heap.heapify(ind)
        else:
            heap.decrease_key(ind, int(info[2]))
    elif info[0] == '3':
        bought = heap.extract_top()
        print(bought[1] + " " + str(day_counter))
