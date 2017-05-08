def mergeSort(alist):
    if len(alist) <= 1:
        return alist

    left = mergeSort(alist[:len(alist)//2])
    right = mergeSort(alist[len(alist)//2:])
    merged = []
    while len(left) > 0 and len(right) > 0:
        merged.append(left.pop(0) if left[0] <= right[0] else right.pop(0))

    merged.extend(mergeSort(left) if len(left) > 0 else mergeSort(right))

    return merged

alist = [54, 26, 93, 17, 77, 31, 44, 55, 20]

alist = mergeSort(alist)

print(alist)
