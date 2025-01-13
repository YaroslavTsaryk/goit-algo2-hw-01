import random


def partition(l_list, left, right, pivotIndex):
    pivotValue = l_list[pivotIndex]
    print(f"{pivotValue = }")
    # print(f"{right = }")
    l_list[pivotIndex], l_list[right] = l_list[right], l_list[pivotIndex]
    storeIndex = left
    for i in range(left, right):
        if l_list[i] < pivotValue:
            print(f"CHANGE {i} {storeIndex}")
            l_list[storeIndex], l_list[i] = l_list[i], l_list[storeIndex]
            print(l_list)
            storeIndex += 1
    l_list[right], l_list[storeIndex] = l_list[storeIndex], l_list[right]
    return storeIndex


def select(l_list, left, right, k):
    print(f"{l_list = }")
    print(f"{left = }")
    print(f"{right = }")
    print(f"{k = }")
    if left == right:
        return l_list[left]
    pivotIndex = random.randint(left, right)
    print(f"{pivotIndex = }")
    # ...     // select a pivotIndex between left and right,
    #                      // e.g., left + floor(rand() % (right − left + 1))
    pivotIndex = partition(l_list, left, right, pivotIndex)
    # // The pivot is in its final sorted position
    if k == pivotIndex:
        return l_list[k]
    elif k < pivotIndex:
        return select(l_list, left, pivotIndex - 1, k)
    else:
        return select(l_list, pivotIndex + 1, right, k)


a = [1, 3, 5, 9, 3, 4, -5, 17, 23, 34, 54, 7, 12, 3, 4, 9, 56, 34, 5]

print("search for element in 8 position")
print(f"FROM QUICK SELECT {select(a, 0, len(a) - 1, 8)}")
print(a)

print(f"FROM SORTED  {sorted(a)[8]}")
print(sorted(a))
