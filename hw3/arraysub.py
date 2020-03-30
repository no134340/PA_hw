"""
ZADATAK 4

ARRAYSUB - subarrays [SPOJ #10582]

Idea:
    Brute force approach a bit optimized.
    Not the best solution (O(k*(n-k) worst case,
    slighly better average case.)
"""

n = int(input())

elems = input()
arr = elems.split(' ')
k = int(input())
result = []

max_ind = 0
for i in range(1, k):
    if arr[i] > arr[max_ind]:
        max_ind = i

result.append(arr[max_ind])

for i in range(1, n - k + 1):
    r = i + k - 1
    if max_ind >= i:
        if arr[r] > arr[max_ind]:
            max_ind = r
    else:
        max_ind = i
        for j in range(i + 1, r + 1):
            if arr[j] > arr[max_ind]:
                max_ind = j
    result.append(arr[max_ind])

output = ' '.join(result)

print(output)
