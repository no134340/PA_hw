def merge(left, right):
    arr = []
    n = len(right) + len(left)
    left.append('a')
    right.append('a')
    lind, rind = 0, 0
    for i in range(n):
        if left[lind] > right[rind]:
            arr.append(right[rind])
            rind += 1
        else:
            arr.append(left[lind])
            lind += 1
    return arr


def merge_sort(arr):
    if len(arr) > 1:
        div = len(arr) // 2
        left_array = merge_sort(arr[:div])
        right_array = merge_sort(arr[div:])
        sorted_arr = merge(left_array, right_array)
        return sorted_arr
    else:
        return arr


big_list = []
big_dict = []
t = int(input())
for i in range(t):
    n = int(input())
    accs = set()
    accs_dict = {}
    for j in range(n):
        acc = input()
        acc_raw = acc.strip(' \n')
        if acc_raw not in accs:
            accs.add(acc_raw)
            accs_dict[acc_raw] = 1
        else:
            accs_dict[acc_raw] += 1
    input()
    big_dict.append(accs_dict)
    big_list.append(merge_sort(list(accs)))

for i in range(len(big_list)):
    case = big_list[i]
    d = big_dict[i]
    for elem in case:
        print("{} {}".format(elem, d[elem]))
    print('')
