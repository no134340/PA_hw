# TODO
"""
Sphere Online Judge problem (SPOJ) #34875
MINSTOCK - Minimum Stocks
"""
from custom_heap import MinHeap

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


day_counter = 1

instr_counter = int(input())
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
