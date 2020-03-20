"""
ZADATAK 4
Sphere Online Judge problem (SPOJ) #34875
MINSTOCK - Minimum Stocks

Using a dictionary.
SPOJ accepted the solution with 4.63s and 9.3M

Idea:
    Use a dictionary to store price-stock pairs.
    Linear search for minimum stock price.

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
from math import inf

day_counter = 0
dict = {}

instr_counter = int(input())
for x in range(instr_counter):
    day_counter += 1
    instruction = str(input()).strip(' \n')
    info = instruction.split(' ')
    if info[0] == '1' or info[0] == '2':
        dict[info[1]] = int(info[2])
    elif info[0] == '3':
        min = inf
        min_key = None
        for key, val in dict.items():
            if val < min:
                min_key = key
                min = val
        dict.pop(min_key)
        print(min_key + " " + str(day_counter))
