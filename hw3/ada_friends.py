"""
ZADATAK 3

ADAFRIEN - Ada and Friends [SPOJ #32944]

Idea:
    Use a dictionary to store friend : expense pairs.
    Convert it to a list, sort it in reverse order and
    the take the first k (if k is greater than the number
    of friends, take them all).
    (Sorting algorithm used: Tim sort. Counting sort would be
    great because we could end up using only last k numbers
    in the list, but the inputs are really large (>10^6)
    so it would be too much auxiliary space used.)
"""

params = input().split(' ')
n, k = int(params[0]), int(params[1])
friend_number = 0
friends = {}
for i in range(n):
    info = input().split(' ')
    friend = info[0]
    money = int(info[1])
    friends[friend] = friends.get(friend, 0) + money

friends_list = []
for key, value in friends.items():
    friends_list.append([key, value])

friends_list.sort(key=lambda expense: expense[1], reverse=True)
sum = 0
for sth, val in friends_list:
    if k <= 0:
        break
    k -= 1
    sum += val
print(sum)
